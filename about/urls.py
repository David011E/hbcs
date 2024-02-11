from .views import ReviewViews, my_json_view
from django.urls import path

urlpatterns = [
    path('', ReviewViews.as_view(), name='about'),
    path('my-json-view/', my_json_view, name='my_json_view'),
    # other URL patterns
]