from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Booking)
class Booking(SummernoteModelAdmin):
    list_display = ('user', 'date' , 'time', 'status')
    list_filter = ['status']
    summernote_fields = ('content',)

# Register your models here.