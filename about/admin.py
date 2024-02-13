from django.contrib import admin
from .models import Reviews
from django_summernote.admin import SummernoteModelAdmin
from django.utils.safestring import mark_safe

@admin.register(Reviews)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'safe_content', 'created_on')
    search_fields = ['title', 'author']
    list_filter = ('created_on', 'author')

    def safe_content(self, obj):
        return mark_safe(obj.content)

    safe_content.short_description = 'Content'
