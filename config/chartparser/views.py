from .forms import YMusiChartForm
from .models import YandexMusicChart, SpotifyChart, LastFMChart
from .services import yandex_music_chart_parsing, spotify_chart_parsing, lastfm_chart_parsing
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


def index(request):
    data = {'header': 'Hello', 'message': 'Make your choice of music chart'}
    return render(request, 'index.html', context=data)


def details(request):
    return HttpResponsePermanentRedirect('/')


def yandex_music_chart_search(request):
    if request.method == "POST":
        form = YMusiChartForm(request.POST)
        if form.is_valid():
            author_name = form.cleaned_data['author_name']
            charts_filter = YandexMusicChart.objects.filter(author_name=author_name)
            data = {'header': 'Yandex Music Chart', 'message': 'Searching results:', 'charts': charts_filter}
            return render(request, 'chart.html', context=data)
        else:
            return HttpResponse('Invalid author name')
    else:
        form = YMusiChartForm()
        return render(request, 'search.html', {'form': form})

def yandex_music_chart(request):
    yandex_music_chart_parsing()
    full_charts = YandexMusicChart.objects.order_by('chart_position')
    data = {'header': 'Yandex Music Chart', 'message': 'Welcome to full Yandex Music chart', 'charts': full_charts}
    return render(request, 'chart.html', context=data)

def spotify_chart(request):
    spotify_chart_parsing()
    full_charts = SpotifyChart.objects.order_by('chart_position')
    data = {'header': 'Spotify', 'message': 'Welcome to full Spotify Music chart', 'charts': full_charts}
    return render(request, 'chart.html', context=data)

def lastfm_chart(request):
    lastfm_chart_parsing()
    full_charts = LastFMChart.objects.order_by('chart_position')
    data = {'header': 'Last FM', 'message': 'Welcome to full Last FM Music chart', 'charts': full_charts}
    return render(request, 'chart.html', context=data)