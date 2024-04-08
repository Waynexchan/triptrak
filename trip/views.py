from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView , UpdateView, DeleteView
from django.db.models import Q
from django.utils.dateparse import parse_date

from .forms import TripForm

from .models import Trip, Note
import os


# Create your views here.
class HomeView(TemplateView):
    template_name ='trip/index.html'

def trip_list(request):
    trips = Trip.objects.filter(owner= request.user)

    context={
        'trips':trips
    }
    return render(request, 'trip/trips_list.html', context)

def trip_search(request):
    search_query = request.GET.get('search', '')
    start_date_query = request.GET.get('start_date', '')

    trips = Trip.objects.filter(owner=request.user)
    
    if search_query:
        trips = trips.filter(Q(city__icontains=search_query) | Q(country__icontains=search_query))
    
    if start_date_query:
        start_date = parse_date(start_date_query)

        if start_date:
            trips = trips.filter(start_date=start_date)

    context = {
        'trips': trips,
        'search_query': search_query,
        'start_date_query': start_date_query,
    }
    return render(request, 'trip/trip_search.html', context)

class TripCreateView(CreateView):
    model = Trip
    form_class = TripForm
    template_name = 'trip/trip_form.html'
    success_url = reverse_lazy('trip-list')  # Use the named URL 'trip-list'

    def form_valid(self, form):
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
    form_class = TripForm 
    template_name = 'trip/trip_form.html'
    success_url = reverse_lazy('trip-list')

    def get_initial(self):
        initial = super().get_initial()
        initial['latitude'] = self.object.latitude
        initial['longitude'] = self.object.longitude
        return initial
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trip'] = self.get_object() # 确保'trip'对象存在于上下文中
        return context
    # template named model_form trip_form
    # don't need get_form because we don't need to limit the usage

class TripDeleteView(DeleteView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    # no template needed -send a post request to this url