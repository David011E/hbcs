from . import views
from .views import BookingView, get_available_time_slots
from django.urls import path

urlpatterns = [
    path('', BookingView.as_view(), name='booking'),
    path('ajax/get_available_time_slots/', get_available_time_slots, name='get_available_time_slots'),
    # other URL patterns
]