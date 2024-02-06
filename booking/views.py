from django.shortcuts import render
from django.views import generic
from .models import Booking

# Create your views here.
class BookingView(generic.ListView):
    queryset = Booking.objects.all()
    template_name = "booking/booking.html"
