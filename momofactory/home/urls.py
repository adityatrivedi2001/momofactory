from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.feedback_view, name='index'),
    # path('', views.news_view, name='index'),
    # path('', views.menu_view, name='index'),
    path('/about', views.about, name='about'),
    path('/blog', views.blog, name='blog'),
    path('/gallery', views.gallery, name='gallery'),
    path('menu', views.menu, name='menu'),
    path('/team', views.team, name='team'),
    path('singleblog/<int:id>', views.singleblog, name='singleblog')
    ]