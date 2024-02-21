from django.shortcuts import render

# Create your views here.
def user_profile(request):
    template_name = "userProfile/user_profile.html"

    return render(
        request,
        template_name,
    )