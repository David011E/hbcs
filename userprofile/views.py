from django.shortcuts import render, get_object_or_404, redirect
from about.models import Reviews
from booking.models import Booking
from django.http import JsonResponse
from django.contrib import messages
import json

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def user_profile(request):
    template_name = "userProfile/user_profile.html"

    # Filters bookings to only those created by the logged-in user
    bookings = Booking.objects.filter(user=request.user)

    # Filters reviews to only those created by the logged-in user
    reviews = Reviews.objects.filter(author=request.user)

    # Combines bookings and reviews into a single dictionary for template context
    context = {'reviews': reviews, 'bookings': bookings}

    # Renders the template with the combined context
    return render(request, template_name, context)


def review_edit(request, content_id):
    """
    view to edit Review
    """
    review = get_object_or_404(Reviews, pk=content_id, author=request.user)

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            review.content = data.get('content', '')
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review successfully updated.')
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
        
        # If the request is not POST, redirect to the user profile page
    return redirect('user_profile')

def delete_review(request, content_id):
    """
    view to delete Review
    """
    review = get_object_or_404(Reviews, pk=content_id, author=request.user)

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            review.content = data.get('content', '')
            review.delete()
            messages.add_message(request, messages.SUCCESS, 'Review successfully deleted.')
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})