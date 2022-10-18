from .models import Order, OrderDetail
from rest_framework import serializers


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = ('status',)


class OrderStatusSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('order_number', 'status')

    def get_status(self, obj):

        ORDER_HIERARCHY = {0:'CANCELLED',
                            1:'SHIPPED',
                            2:'PENDING'}

        queryset = OrderDetail.objects.filter(order_number=obj)
        order_lines = OrderDetailSerializer(queryset, many=True, read_only=True)
        status = list(set([value['status'] for value in order_lines.data]))
        
        if len(status) == 1:
            return status[0]
        elif len(status) == 2 and ORDER_HIERARCHY[0] in status:
            for order_status in status:
                if order_status != ORDER_HIERARCHY[0]:
                    return order_status
        else:
            return ORDER_HIERARCHY[2]


