from django.shortcuts import render, redirect
from django.views import View
from .models import Booking
from .forms import BookingForm
from django.contrib import messages
from datetime import datetime
from django.utils import timezone
from django.http import JsonResponse

class BookingView(View):
    queryset = Booking.objects.all()
    template_name = "booking/booking.html"

    def get(self, request):
        time_slots = Booking.TIME_SLOTS
        disabled_time_slots = self.get_disabled_time_slots()
        booking_form = BookingForm(time_slots=time_slots, disabled_time_slots=disabled_time_slots)
        
        return render(request, self.template_name, {'booking_form': booking_form, 'disabled_time_slots': disabled_time_slots})

    def get_disabled_time_slots(self):
        current_datetime = datetime.now()
        booked_time_slots = Booking.objects.filter(date__gte=current_datetime.date(), status=1).values_list('time', flat=True)

        return list(booked_time_slots) if booked_time_slots else []

    def post(self, request):
        time_slots = Booking.TIME_SLOTS  # Assuming you have defined TIME_SLOTS in your Booking model
        booking_form = BookingForm(data=request.POST, time_slots=time_slots)
        if booking_form.is_valid() and booking.user == request.user:
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.status = 1  # Assuming all bookings are immediately set to 'Booked' upon form submission
            booking.save()
            messages.add_message(request, messages.SUCCESS, 'Booking Success')
            return redirect('user_profile')
        else:
            return render(request, self.template_name, {'booking_form': booking_form})


def get_available_time_slots(request):
    date = request.GET.get('date', None)
    if date:
        try:
            date_obj = datetime.strptime(date, '%Y-%m-%d').date()
            current_datetime = timezone.now()
            if date_obj == current_datetime.date():  # If the date is today, filter out past time slots
                current_time = current_datetime.time()
                all_time_slots = Booking.TIME_SLOTS
                time_slots_info = [{'time': slot[0], 'booked': False} if datetime.strptime(date + ' ' + slot[0], '%Y-%m-%d %H:%M').time() >= current_time else {'time': slot[0], 'booked': True} for slot in all_time_slots]
            else:
                booked_time_slots = Booking.objects.filter(date=date_obj).values_list('time', flat=True)
                all_time_slots = Booking.TIME_SLOTS
                time_slots_info = [{'time': slot[0], 'booked': slot[0] in booked_time_slots} for slot in all_time_slots]
            return JsonResponse({'time_slots': time_slots_info})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'No date provided'}, status=400)