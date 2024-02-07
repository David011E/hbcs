from django.contrib import admin
from .models import Reviews
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Reviews)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'content', 'created_on')
    search_fields = ['title', 'author']
    list_filter = ('created_on', 'author')
    summernote_fields = ('content',)

# Register your models here.