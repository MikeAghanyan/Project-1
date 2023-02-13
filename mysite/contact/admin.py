from django.contrib import admin
from .models import ContactUs

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email']
    list_display_links = ['id', 'full_name', 'email']
    search_fields = ['id', 'full_name', 'email']