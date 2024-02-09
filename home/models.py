from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Image(models.Model):
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.CharField(max_length=200, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)