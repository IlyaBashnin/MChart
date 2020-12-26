from django.urls import path
from django.urls import re_path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.index),
    re_path(r'^about', TemplateView.as_view(template_name="about.html")),
    re_path(r'^contact', TemplateView.as_view(template_name="contact.html")),
    re_path(r'^yamusic', views.yamusic_parsing),
    re_path(r'^details', views.details),
]
