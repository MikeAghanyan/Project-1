from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('about/', views.about, name='about'),    
    # path('detail_page/', views.detail_page, name='detail_page'),
    path('listing_page/', views.listing_page, name='listing_page'),
    path('detail_page/<int:id>', views.IndexDetailView.as_view(), name='detail_page'),
    # path('listing_page/<int:id>', views.IndexCategory.as_view(), name='listing_page'),
]