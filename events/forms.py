from .models import Register_data
from django import forms


class EventForm(forms.ModelForm):
    class Meta:
        model = Register_data
        fields = ['attendee', 'event']
