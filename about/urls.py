from .views import ReviewViews
from django.urls import path

urlpatterns = [
    path('', ReviewViews.as_view(), name='reviews'),
    # other URL patterns
]