from .models import YandexMusicChart
from bs4 import BeautifulSoup
import csv
import requests

URL = 'https://music.yandex.by/chart/tracks'


def yandex_music_chart_parsing() -> None:
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'lxml')
    tracks = soup.find_all('div', class_='d-track__name')
    authors = soup.find_all('div', class_='d-track__meta')
    for i in range(len(tracks)):
        yandex_music_chart = YandexMusicChart(chart_position=i,
                                              track_name=tracks[i].text,
                                              author_name=authors[i].text)
        yandex_music_chart.save()
