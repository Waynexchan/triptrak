from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('account_activation_sent')
    template_name = 'registration/signup.html'    

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save(commit=False)
        user.is_active = False  
        user.save()
        send_activation_email(self.request, user)  
        return response

UserModel = get_user_model()


def send_activation_email(request, user):
    token = default_token_generator.make_token(user)
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    activation_link = request.build_absolute_uri(
        reverse('activate', kwargs={'uidb64': uidb64, 'token': token})
    )
    
    subject = 'Activate your account'
    message = f'Hi {user.username}, Please click the link to activate your account: {activation_link}'
    from_email = 'your-gmail-address@gmail.com'
    send_mail(subject, message, from_email, [user.email], fail_silently=False)

def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        # 登入用戶
        # 重定向到主頁面或顯示成功頁面
        return redirect('home')
    else:
        # 顯示失敗頁面
        return render(request, 'activation_failed.html', {})
    
def account_activation_sent(request):
    return render(request, 'registration/account_activation_sent.html')
    
def resend_activation_link(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = UserModel.objects.get(email=email)  
            if not user.is_active:
                send_activation_email(request, user)  
                return render(request, 'registration/activation_email_sent.html')
            else:
               
                return render(request, 'registration/user_already_active.html')
        except UserModel.DoesNotExist:  
            return render(request, 'registration/user_not_found.html')

    return render(request, 'registration/resend_activation_link.html')