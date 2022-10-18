from django.urls import path
from .views import OrderSeasonsView


urlpatterns = [
    path('', OrderSeasonsView.as_view(), name='order_seasons_view'),
]