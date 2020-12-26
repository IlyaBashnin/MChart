from .forms import YMusiChartForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

from .models import YandexMusicChart
from bs4 import BeautifulSoup
import csv
import requests


# URL = 'https://music.yandex.by/chart/tracks'


def index(request):
    authors = ['ONE', 'TWO', 'THREE']
    data = {'header': 'Hello', 'message': 'Welcome to YMusiChart parser', 'authors': authors}
    return render(request, 'index.html', context=data)


def details(request):
    return HttpResponsePermanentRedirect('/')


def yamusic_parsing(request):
    if request.method == "POST":
        form = YMusiChartForm(request.POST)
        if form.is_valid():
            author_name = form.cleaned_data['author_name']
            return HttpResponse('<h2>Looking {0}</h2>'.format(author_name))
        else:
            return HttpResponse('Invalid author name')
    else:
        form = YMusiChartForm()
        return render(request, 'chart.html', {'form': form})


# if __name__=="__main__":
#     response = requests.get(URL)
#     soup = BeautifulSoup(response.text, 'lxml')
#     quotes = soup.find_all('div', class_='d-track__name')
#     authors = soup.find_all('div', class_='d-track__meta')
#     for i in range(0, len(quotes)):
#         print(i+1, quotes[i].text, authors[i].text,  sep=' || ')
