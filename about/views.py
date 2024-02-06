from django.shortcuts import render
from django.views import generic
from .models import Reviews

# Create your views here.
class ReviewViews(generic.ListView):
    queryset = Reviews.objects.all()
    template_name = "about/about.html"