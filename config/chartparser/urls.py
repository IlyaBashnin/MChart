from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.index),
    re_path(r'^about', views.about),
    re_path(r'^contact', views.contact),
    re_path(r'^yamusic', views.yamusic_parsing),
    re_path(r'^details', views.details),
]
