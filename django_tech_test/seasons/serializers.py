from .models import CustomerOrder
from rest_framework import serializers
import datetime


class OrderSeasonsSerializer(serializers.ModelSerializer):

    SEASON = serializers.SerializerMethodField()

    class Meta:
        model = CustomerOrder
        fields = ('ORD_ID','SEASON')
    
    def get_SEASON(self, obj):

        DUMMY_YEAR = 1950

        seasons = {
                    (datetime.date(DUMMY_YEAR,3,19), datetime.date(DUMMY_YEAR,6,19)):'Spring',
                    (datetime.date(DUMMY_YEAR,6,20), datetime.date(DUMMY_YEAR,9,21)):'Summer',
                    (datetime.date(DUMMY_YEAR,9,22), datetime.date(DUMMY_YEAR,12,20)):'Fall',
                    (datetime.date(DUMMY_YEAR,12,21), datetime.date(DUMMY_YEAR,12,31)):'Winter',
                    (datetime.date(DUMMY_YEAR,1,1), datetime.date(DUMMY_YEAR,3,18)):'Winter',
                    }

        order_date = obj.ORD_DT
        dummy_date = datetime.date(DUMMY_YEAR, order_date.month, order_date.day)

        for (date1, date2) in seasons:
            if (min(date1,date2) <= dummy_date <= max(date1, date2)):
                return seasons[(date1, date2)]
