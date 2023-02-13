from django.shortcuts import render
from .models import HomeCarusel, HomeTopic, HomeLatestEpisode, HomeTrendingEpisode, AboutPodcaster
from django.views.generic import ListView, DetailView 


class IndexListView(ListView):
    template_name = 'pages/index.html'

          
    def get(self, request):

        home_carusel_list=HomeCarusel.objects.all()
        home_topic_list=HomeTopic.objects.all()
        home_latest_episodes_list=HomeLatestEpisode.objects.all()
        home_trending_episodes_list=HomeTrendingEpisode.objects.all()
        return render(request, 'pages/index.html', context={'home_carusel_list':home_carusel_list, 
                                                            'home_topic_list':home_topic_list,
                                                            'home_trending':home_trending_episodes_list,
                                                            'home_latest':home_latest_episodes_list})

class IndexDetailView(DetailView):
    template_name = 'pages/detail-page.html'
    
    def get(self, request, id):
        topic_detail = HomeTopic.objects.get(pk=id)
        trending_detail = HomeTrendingEpisode.objects.all()[:4]
        return render(request, self.template_name, context={'topic_detail':topic_detail,
                                                            'trending_detail':trending_detail,
                                                            }) 



def about(request):
    about_podcaster_list=HomeCarusel.objects.all()[:4]
    return render(request, 'pages/about.html', context={'about_podcaster':about_podcaster_list})



def detail_page(request):
    return render(request, 'pages/detail-page.html')

def listing_page(request):
    return render(request, 'pages/listing-page.html')