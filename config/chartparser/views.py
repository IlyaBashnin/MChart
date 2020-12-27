from .forms import YMusiChartForm
from .models import YandexMusicChart
from .services import yandex_music_chart_parsing
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


def index(request):
    authors = ['ONE', 'TWO', 'THREE', '66677', '77556']
    yandex_music_chart_parsing()
    # x = YandexMusicChart(chart_position='5', track_name='Track5', author_name='Author5')
    # x.save()
    y = YandexMusicChart.objects.order_by('chart_position')
    data = {'header': 'Hello', 'message': 'Welcome to YMusiChart parser', 'authors': y}
    return render(request, 'index.html', context=data)


def details(request):
    return HttpResponsePermanentRedirect('/')


def yamusic_parsing(request):
    if request.method == "POST":
        form = YMusiChartForm(request.POST)
        if form.is_valid():
            author_name = form.cleaned_data['author_name']
            y = YandexMusicChart.objects.filter(author_name = author_name)
            data = {'header': 'Hello', 'message': 'Welcome to YMusiChart parser', 'authors': y}
            return render(request, 'index.html', context=data)
        else:
            return HttpResponse('Invalid author name')
    else:
        form = YMusiChartForm()
        return render(request, 'chart.html', {'form': form})
