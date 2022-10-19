from django.db import models


class WeatherDate(models.Model):

    date = models.DateField()
    was_rainy = models.BooleanField()

    def __str__(self):
        return f'{self.date - self.was_rainy}'
