from .models import YandexMusicChart
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from pprint import pprint
import csv
import requests


# URL = 'https://music.yandex.by/chart/tracks'


def index(request):
    authors = ['First', 'Second', 'Third']
    data = {'header': 'Hello Django', 'message': 'Welcome to YMusiChart parser', 'authors': authors}
    return render(request, 'index.html', context=data)


def details(request):
    return HttpResponsePermanentRedirect('/')


def yamusic_parsing(request):
    author_name = request.GET.get('author', '')
    output = '<h2>Author:</h2><h3>{0}'.format(author_name)
    return HttpResponse(output)


# if __name__=="__main__":
#     response = requests.get(URL)
#     soup = BeautifulSoup(response.text, 'lxml')
#     quotes = soup.find_all('div', class_='d-track__name')
#     authors = soup.find_all('div', class_='d-track__meta')
#     for i in range(0, len(quotes)):
#         print(i+1, quotes[i].text, authors[i].text,  sep=' || ')
