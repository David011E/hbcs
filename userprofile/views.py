from django.shortcuts import render, get_object_or_404, redirect
from about.models import Reviews
from django.http import JsonResponse
from django.contrib import messages
import json

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required # Ensures that only logged-in users can access this view
def user_profile(request):
    template_name = "userProfile/user_profile.html"

    # Filters reviews to only those created by the logged-in user
    reviews = Reviews.objects.filter(author=request.user)
    return render(request, template_name, {'reviews': reviews})


def review_edit(request, content_id):
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