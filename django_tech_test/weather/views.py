from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import WeatherDateSerializer
from .models import WeatherDate


class WeatherDateView(APIView):

    def get(self, request):
        queryset = WeatherDate.objects.filter(was_rainy=True)
        serializer = WeatherDateSerializer(queryset, many=True)
        data_filtered = [data for data in serializer.data if data['changed_to_bad'] == True]

        return Response(data_filtered)
