from django.db import models


class YandexMusicChart(models.Model):
    chart_position = models.PositiveSmallIntegerField()
    track_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=50)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Chart'
        db_table = 'yandex_music_chart'
