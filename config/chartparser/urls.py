from django.urls import path
from django.urls import re_path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.index),
    re_path(r'^about', TemplateView.as_view(template_name="about.html")),
    re_path(r'^contact', TemplateView.as_view(template_name="contact.html")),
    re_path(r'^search', views.yandex_music_chart_search),
    re_path(r'^index', views.details),
    re_path(r'^yandex', views.yandex_music_chart),
    re_path(r'^spotify', views.spotify_chart),
    re_path(r'^lastfm', views.lastfm_chart),
]
