from django.db import models


class SeasonOrder(models.Model):

    ORD_ID = models.CharField(max_length=100)
    ORD_DT = models.DateField()
    QT_ORDD = models.IntegerField()

    def __str__(self):
        return self.ORD_ID
