from .models import YandexMusicChart, SpotifyChart, LastFMChart
from bs4 import BeautifulSoup
import requests

URL_YANDEX = 'https://music.yandex.by/chart/tracks'
URL_SPOTIFY = 'https://spotifycharts.com/regional'
URL_LASTFM = 'https://www.last.fm/ru/charts'


def yandex_music_chart_parsing() -> None:
    response = requests.get(URL_YANDEX)
    soup = BeautifulSoup(response.text, 'lxml')
    tracks = soup.find_all('div', class_='d-track__name')
    authors = soup.find_all('div', class_='d-track__meta')
    for i in range(len(tracks)):
        if YandexMusicChart.objects.filter(chart_position=i + 1,
                                           track_name=tracks[i].text,
                                           author_name=authors[i].text).exists():
            pass
        else:
            yandex_music_chart = YandexMusicChart(chart_position=i + 1,
                                                  track_name=tracks[i].text,
                                                  author_name=authors[i].text)
            yandex_music_chart.save()

def spotify_chart_parsing() -> None:
    response = requests.get(URL_SPOTIFY)
    soup = BeautifulSoup(response.text, 'lxml')
    tracks_authors = soup.find_all('td', class_='chart-table-track')
    for i in range(len(tracks_authors)):
        out = [x for x in tracks_authors[i].text.splitlines() if x != '']
        if SpotifyChart.objects.filter(chart_position=i + 1,
                                       track_name=out[0],
                                       author_name=out[1].strip("by ")).exists():
            pass
        else:
            spotify_music_chart = SpotifyChart(chart_position=i + 1,
                                               track_name=out[0],
                                               author_name=out[1].strip("by "))
            spotify_music_chart.save()


def lastfm_chart_parsing() -> None:
    response = requests.get(URL_LASTFM)
    soup = BeautifulSoup(response.text, 'lxml')
    global_chart = soup.find('table', class_='globalchart')
    tracks = global_chart.find_all('td', class_='globalchart-name')
    artists = global_chart.find_all('td', class_='globalchart-track-artist-name')
    for i in range(len(tracks)):
        out = [x for x in tracks[i].text.splitlines() + artists[i].text.splitlines() if x != '']
        if LastFMChart.objects.filter(chart_position=i + 1,
                                      track_name=out[0],
                                      author_name=out[1]).exists():
            pass
        else:
            lastfm_chart = LastFMChart(chart_position=i + 1,
                                        track_name=out[0],
                                        author_name=out[1])
            lastfm_chart.save()


# def soup_cooking(url_source: str) -> BeautifulSoup:
#     response = requests.get(url_source)
#     soup = BeautifulSoup(response.text, 'lxml')
#     return soup
#
#
# def printer(data) -> None:
#     print(f'{data[0]} || {data[1].strip("by ")}')
#
#
# def yandex_music_chart_parser(soup: BeautifulSoup):
#     tracks = soup.find_all('div', class_='d-track__name')
#     authors = soup.find_all('div', class_='d-track__meta')
#     for i in range(len(tracks)):
#         out = [tracks[i].text] + [authors[i].text]
#         printer(out)
#
#
# def spotify_chart_parser(soup: BeautifulSoup):
#     tracks_authors = soup.find_all('td', class_='chart-table-track')
#     for i in range(len(tracks_authors)):
#         out = [x for x in tracks_authors[i].text.splitlines() if x != '']
#         printer(out)
#
#
# def lastfm_chart_parser(soup: BeautifulSoup):
#     global_chart = soup.find('table', class_='globalchart')
#     tracks = global_chart.find_all('td', class_='globalchart-name')
#     artists = global_chart.find_all('td', class_='globalchart-track-artist-name')
#     for i in range(len(tracks)):
#         out = [x for x in tracks[i].text.splitlines() + artists[i].text.splitlines() if x != '']
#         printer(out)
#
#
# yandex_music_chart_parser(soup_cooking(URL_YANDEX))
# spotify_chart_parser(soup_cooking(URL_SPOTIFY))
# lastfm_chart_parser(soup_cooking(URL_LASTFM))
