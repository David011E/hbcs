from django.contrib import admin
from .models import Reviews
from django_summernote.admin import SummernoteModelAdmin
from django.utils.safestring import mark_safe

@admin.register(Reviews)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('author', 'safe_content', 'created_on')
    search_fields = ['author']
    list_filter = ('created_on', 'author')
    summernote_fields = ['content']
    

    def safe_content(self, obj):
        return mark_safe(obj.content)

    safe_content.short_description = 'Content'
