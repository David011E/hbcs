from django.shortcuts import render
from about.models import Reviews
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required # Ensures that only logged-in users can access this view
def user_profile(request):
    template_name = "userProfile/user_profile.html"

    # Filters reviews to only those created by the logged-in user
    reviews = Reviews.objects.filter(author=request.user)
    return render(request, template_name, {'reviews': reviews})