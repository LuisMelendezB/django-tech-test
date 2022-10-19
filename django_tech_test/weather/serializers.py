from .models import WeatherDate
from rest_framework import serializers
import datetime


class WeatherDateSerializer(serializers.ModelSerializer):

    changed_to_bad = serializers.SerializerMethodField()

    class Meta:
        model = WeatherDate
        fields = ('date','changed_to_bad')

    def get_changed_to_bad(self, obj):
        prev_date = obj.date - datetime.timedelta(days=1)
        prev_obj = WeatherDate.objects.filter(date=prev_date).first()
        if prev_obj:
            if prev_obj.was_rainy == False and obj.was_rainy == True:
                return True
            else:
                return False
        else:
            return False



