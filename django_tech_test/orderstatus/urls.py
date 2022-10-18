from django.urls import path
from .views import OrderStatusView


urlpatterns = [
    path('', OrderStatusView.as_view(), name='order_status_view'),
]