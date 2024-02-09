from django.contrib import admin
from .models import Image
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Image)
class Image(SummernoteModelAdmin):
    list_display = ('featured_image', 'description', 'uploaded_at')
    list_filter = ['uploaded_at']
    summernote_fields = ['content']