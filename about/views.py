import os
import json
from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Reviews

# Create your views here.
class ReviewViews(generic.ListView):
    queryset = Reviews.objects.all()
    template_name = "about/about.html"

    def get_context_data(self):
        context = super().get_context_data()

        # Get all reviews and order them by created_on
        context['reviews'] = Reviews.objects.all().order_by("-created_on")

        # Get the count of all reviews
        context['review_count'] = Reviews.objects.count()

        # Add the JSON data to the context
        json_file_path = os.path.join(settings.BASE_DIR, 'data', 'company.json')
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

        context['company'] = data

        return context

@csrf_exempt
def my_json_view(request):
    data = []

    # Path to your JSON file
    json_file_path = os.path.join(settings.BASE_DIR, 'data', 'company.json')

    # Read JSON data from the file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    return JsonResponse(data, safe=False)
