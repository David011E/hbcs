from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.utils.html import strip_tags

class Reviews(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer")
    content = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now=True)
    excerpt = models.TextField(blank=True)

    class Meta:
        ordering = ["created_on"]

    def safe_content(self):
        return mark_safe(self.content)

    safe_content.short_description = 'Content'

    def clean_content(self):
        return strip_tags(self.content)

    def __str__(self):
        return f"{self.clean_content()} | by {self.author}"
