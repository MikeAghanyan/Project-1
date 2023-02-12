from django.contrib import admin
from .models import HomeCarusel, HomeTopic

@admin.register(HomeCarusel)
class HomeCaruselAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name'] 

@admin.register(HomeTopic)
class HomeTopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'topic', 'i_count']
    list_display_links = ['id', 'topic']
    search_fields = ['topic']