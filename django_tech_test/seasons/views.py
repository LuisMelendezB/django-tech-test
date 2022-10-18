from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSeasonsSerializer
from .models import CustomerOrder

class OrderSeasonsView(APIView):

    def get(self, request):
        queryset = CustomerOrder.objects.all()
        serializer = OrderSeasonsSerializer(queryset, many=True)
        return Response(serializer.data)
