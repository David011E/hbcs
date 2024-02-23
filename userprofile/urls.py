from . import views
from django.urls import path
from .views import review_edit, delete_review, cancel_booking

urlpatterns = [
    path('', views.user_profile, name='user_profile'),
    path('edit_review/<int:content_id>/', review_edit, name='review_edit'),  # If you're using the review_edit view
    path('delete_review/<int:content_id>/', delete_review, name='delete_review'),  
    path('cancel_booking/<int:booking_id>/', cancel_booking, name='cancel_booking'),
]