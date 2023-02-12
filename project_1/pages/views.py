from django.shortcuts import render
from .models import HomeCarusel, HomeTopic

def index(request):
    home_carusel_list=HomeCarusel.objects.all()
    home_topic_list=HomeTopic.objects.all()
    return render(request, 'pages/index.html', context={'home_carusel_list':home_carusel_list, 'home_topic_list':home_topic_list})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def detail_page(request):
    return render(request, 'pages/detail-page.html')

def listing_page(request):
    return render(request, 'pages/listing-page.html')