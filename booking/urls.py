from . import views
from .views import BookingView
from django.urls import path

urlpatterns = [
    path('', BookingView.as_view(), name='booking'),
    # other URL patterns
]