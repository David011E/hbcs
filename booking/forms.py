from django import forms
from django.utils import timezone
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('date', 'time')

    def __init__(self, *args, **kwargs):
        time_slots = kwargs.pop('time_slots', None)
        disabled_time_slots = kwargs.pop('disabled_time_slots', None) or []  # Get the disabled time slots
        super(BookingForm, self).__init__(*args, **kwargs)
        
        self.fields['date'] = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
        
        if time_slots:
            choices = []
            for time_slot in time_slots:
                if time_slot in disabled_time_slots:
                    choices.append((time_slot))  # Disable booked time slots
                else:
                    choices.append((time_slot))
            self.fields['time'] = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'disabled': 'disabled'}))
        else:
            self.fields['time'] = forms.ChoiceField(choices=[], widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))

        
        # Get today's date in YYYY-MM-DD format
        today = timezone.localtime(timezone.now()).date().isoformat()
        
        # Set the 'min' attribute of the date field to today's date
        self.fields['date'] = forms.DateField(widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'min': today  # Ensure users cannot pick a date before today
        }))