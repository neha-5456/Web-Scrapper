from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    
   path('', views.home, name='home'),
   path('scrape/', views.scrape, name='scrape'),
   path('download/', views.download_file, name='download_file'),
]
