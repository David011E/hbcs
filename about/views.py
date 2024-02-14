import os
import json
from django.shortcuts import render, redirect
from django.views import generic
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Reviews
from .forms import ReviewForm
from django.contrib import messages

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

        # Initialize an empty review form
        context['review_form'] = ReviewForm()

        return context

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            review_form = ReviewForm(data=request.POST)
            if review_form.is_valid():
                
                # Save the form data to the Review model
                review = review_form.save(commit=False)
                review.author = request.user
                review.content = review.content
                review.save()

                messages.add_message(
                    request, messages.SUCCESS,
                    'Review Success'
                )

                # Redirect to the same page after successful form submission
                return redirect('about')

        # If the request is not a POST, return the rendered template
        return self.render_to_response(self.get_context_data())



@csrf_exempt
def my_json_view(self, request):
    data = []

    # Path to your JSON file
    json_file_path = os.path.join(settings.BASE_DIR, 'data', 'company.json')

    # Read JSON data from the file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

        return JsonResponse(data, safe=False)
