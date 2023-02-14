from django.shortcuts import render
from .models import HomeCarusel, HomeGenre, HomeEpisode
from django.views.generic import ListView, DetailView 


class IndexListView(ListView):
    template_name = 'pages/index.html'

    def get(self, request):

        home_carusel_list=HomeCarusel.objects.all()
        home_genre_list=HomeGenre.objects.all()
        home_latest_episode_list=HomeEpisode.objects.all()[:2]
        home_episodes_list=HomeEpisode.objects.all()[:3]

        return render(request, 'pages/index.html', context={'home_carusel_list':home_carusel_list, 
                                                            'home_genre_list':home_genre_list,
                                                            'home_latest_episode_list':home_latest_episode_list,
                                                            'home_episode_list':home_episodes_list}) 


class ListingGenre(ListView):
    template_name = 'pages/listing-page.html'
    
    def get(self, request, id):
        
        genre_list = HomeGenre.objects.filter(pk=id)
        
        return render(request, self.template_name, context={'genre_list':genre_list}) 


class IndexDetailView(DetailView):
    template_name = 'pages/detail-page.html'
    
    def get(self, request, slug):

        detail_genre_list = HomeGenre.objects.get(slug=slug)
        detail_episode_list = HomeEpisode.objects.all()[:3]

        return render(request, self.template_name, context={'detail_genre_list':detail_genre_list,
                                                            'detail_episode_list':detail_episode_list,
                                                            }) 



def about(request):
    about_podcaster_list=HomeCarusel.objects.all()[:4]
    return render(request, 'pages/about.html', context={'about_podcaster':about_podcaster_list})


def all_genre(request):
    all_genre_list=HomeGenre.objects.all()
    return render(request, 'pages/all_genre.html', context={'all_genre_list':all_genre_list})
