from django.db import models


class YandexMusicChart(models.Model):
    chart_position = models.PositiveSmallIntegerField()
    track_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=50)

    def __str__(self):
        out = f'{self.chart_position}. | {self.author_name}  -  {self.track_name}'
        return out

    class Meta:
        verbose_name = 'Yandex Music Chart'
        db_table = 'yandex_music_chart'


class SpotifyChart(models.Model):
    chart_position = models.PositiveSmallIntegerField()
    track_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=50)

    def __str__(self):
        out = f'{self.chart_position}. | {self.author_name}  -  {self.track_name}'
        return out

    class Meta:
        verbose_name = 'Spotyfy Chart'
        db_table = 'spotify_chart'


class LastFMChart(models.Model):
    chart_position = models.PositiveSmallIntegerField()
    track_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=50)

    def __str__(self):
        out = f'{self.chart_position}. | {self.author_name}  -  {self.track_name}'
        return out

    class Meta:
        verbose_name = 'LastFM Chart'
        db_table = 'lastfm_chart'
