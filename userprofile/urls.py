from . import views
from django.urls import path
from .views import review_edit

urlpatterns = [
    path('', views.user_profile, name='user_profile'),
    path('edit_review/<int:content_id>/', review_edit, name='review_edit'),  # If you're using the review_edit view
]