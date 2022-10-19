from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderStatusSerializer
from .models import Order


class OrderStatusView(APIView):

    def get(self, request):
        queryset = Order.objects.all()
        serializer = OrderStatusSerializer(queryset, many=True)
        return Response(serializer.data)


