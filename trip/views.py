from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView , UpdateView, DeleteView

from.models import Trip, Note


# Create your views here.
class HomeView(TemplateView):
    template_name ='trip/index.html'

def trip_list(request):
    trips = Trip.objects.filter(owner= request.user)
    context={
        'trips':trips
    }
    return render(request, 'trip/trips_list.html', context)

class TripCreateView(CreateView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields= ['city', 'country', 'start_date', 'end_date']
    #template named model_form.html

    def form_valid(self, form):
        #owner field = logged in user
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class TripDetailView(DetailView):
    model = Trip

    # data stored on trip - also have the Notes date
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip = context['object']
        notes = trip.notes.all()
        context['notes'] = notes
        return context
    
class NoteDetailView(DetailView):
    model = Note

class NoteListView(ListView):
    model = Note
    #model_list.html
    def get_queryset(self):
        queryset = Note.objects.filter(trip__owner=self.request.user)
        return queryset
    
class NoteCreateView(CreateView):
    model = Note
    success_url = reverse_lazy('note-list')
    fields = '__all__'

    def get_form(self):
        form = super(NoteCreateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user) #filter login user
        form.fields['trip'].queryset = trips #just the trips for the login user
        return form
    
class NoteUpdateView(UpdateView):
    model = Note
    success_url = reverse_lazy('note-list')
    fields = '__all__'

    def get_form(self):
        form = super(NoteUpdateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user) #filter login user
        form.fields['trip'].queryset = trips #just the trips for the login user
        return form
    
class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')
    # no template needed -send a post request to this url

class TripUpdateView(UpdateView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ['city', 'country', 'start_date', 'end_date']
    # template named model_form trip_form
    # don't need get_form because we don't need to limit the usage

class TripDeleteView(DeleteView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    # no template needed -send a post request to this url