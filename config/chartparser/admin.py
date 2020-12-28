from django.contrib import admin
from .models import YandexMusicChart, SpotifyChart, LastFMChart

admin.site.register(YandexMusicChart)
admin.site.register(SpotifyChart)
admin.site.register(LastFMChart)