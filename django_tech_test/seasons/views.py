from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SeasonOrderSerializer
from .models import SeasonOrder

class SeasonOrderView(APIView):

    def get(self, request):
        queryset = SeasonOrder.objects.all()
        serializer = SeasonOrderSerializer(queryset, many=True)
        return Response(serializer.data)
