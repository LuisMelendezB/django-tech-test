from .models import Order, OrderDetail
from rest_framework import serializers


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = '__all__'


class OrderStatusSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    
    def get_status(self, obj):
        queryset = OrderDetail.objects.filter(order_number=obj)
        order_lines = OrderDetailSerializer(queryset, many=True, read_only=True)
        status = list(set([value['status'] for value in order_lines.data]))
        
        if len(status) == 1:
            return status[0]
        elif len(status) == 2 and 'CANCELLED' in status:
            for order_status in status:
                if order_status != 'CANCELLED':
                    return order_status
        else:
            return 'PENINDG'


