from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
    latitude = forms.DecimalField(max_digits=20, decimal_places=15)
    longitude = forms.DecimalField(max_digits=20, decimal_places=15)
    
    class Meta:
        model = Trip
        fields = ['city', 'country', 'start_date', 'end_date', 'latitude', 'longitude']
        
        