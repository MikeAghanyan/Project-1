from django.contrib import admin
from .models import HomeCarusel, HomeGenre, HomeEpisode

@admin.register(HomeCarusel)
class HomeCaruselAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name'] 

@admin.register(HomeEpisode)
class HomEpisode(admin.ModelAdmin):
    list_display = ['id', 'name', 'author']
    list_display_links = ['id', 'name', 'author']
    search_fields = ['name', 'author']

@admin.register(HomeGenre)
class HomeGenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'topic', 'i_count']
    list_display_links = ['id', 'topic']
    search_fields = ['topic']
