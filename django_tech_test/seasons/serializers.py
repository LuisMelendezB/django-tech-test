from .models import SeasonOrder
from rest_framework import serializers
from datetime import date


class SeasonOrderSerializer(serializers.ModelSerializer):

    SEASON = serializers.SerializerMethodField()

    class Meta:
        model = SeasonOrder
        fields = ('ORD_ID','SEASON')
    

    def get_SEASON(self, obj):

        DUMMY_YEAR = 1950

        seasons = {
                    (date(DUMMY_YEAR,3,19), date(DUMMY_YEAR,6,19)):'Spring',
                    (date(DUMMY_YEAR,6,20), date(DUMMY_YEAR,9,21)):'Summer',
                    (date(DUMMY_YEAR,9,22), date(DUMMY_YEAR,12,20)):'Fall',
                    (date(DUMMY_YEAR,12,21), date(DUMMY_YEAR,12,31)):'Winter',
                    (date(DUMMY_YEAR,1,1), date(DUMMY_YEAR,3,18)):'Winter',
                    }

        order_date = obj.ORD_DT
        dummy_date = date(DUMMY_YEAR, order_date.month, order_date.day)

        for (date1, date2) in seasons:
            if (min(date1,date2) <= dummy_date <= max(date1, date2)):
                return seasons[(date1, date2)]
