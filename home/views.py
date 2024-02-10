from django.shortcuts import render
from .models import Image

# Create your views here.
def my_home(request):
    image_list = Image.objects.filter(description__icontains='main')
    cert_image_list = Image.objects.filter(description__icontains='cert')
    template_name = "home/index.html"

    return render(
        request, 
        template_name, 
        {'image_list': image_list, 'cert_image_list': cert_image_list}
        )
