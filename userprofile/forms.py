from about.models import Reviews
from booking.models import Booking
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('content',)


class BookingForms(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('user', 'date', 'time', 'status')
