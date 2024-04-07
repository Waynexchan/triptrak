from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # 添加必填的電子郵件字段

    class Meta:
        model = User  # 指定這個表單是基於 User 模型
        fields = ("username", "email", "password1", "password2")
        # 指定表單包含的字段：用戶名、電子郵件、密碼和密碼確認

    def save(self, commit=True):
        user = super().save(commit=False)  # 先調用父類的保存方法，但不立即提交到數據庫
        user.email = self.cleaned_data["email"]  # 將表單中清理後的電子郵件數據賦值給用戶對象
        if commit:
            user.is_active = False  # 設置用戶為非激活狀態
            user.save()  # 真正將用戶數據保存到數據庫
        return user