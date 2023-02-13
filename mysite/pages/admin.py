from django.contrib import admin
from .models import HomeCarusel, HomeTopic, HomeLatestEpisode, HomeTrendingEpisode, AboutPodcaster

@admin.register(HomeCarusel)
class HomeCaruselAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name'] 

@admin.register(HomeLatestEpisode)
class HomeLatestEpisode(admin.ModelAdmin):
    list_display = ['id', 'name', 'author']
    list_display_links = ['id', 'name', 'author']
    search_fields = ['name', 'author']

@admin.register(HomeTopic)
class HomeTopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'topic', 'i_count']
    list_display_links = ['id', 'topic']
    search_fields = ['topic']

@admin.register(HomeTrendingEpisode)
class HomeTrendingEpisode(admin.ModelAdmin):
    list_display = ['id', 'name', 'author']
    list_display_links = ['id', 'name', 'author']
    search_fields = ['name', 'author']

@admin.register(AboutPodcaster)
class AboutPodcaster(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']