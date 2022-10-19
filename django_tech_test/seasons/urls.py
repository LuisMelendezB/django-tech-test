from django.urls import path
from .views import SeasonOrderView


urlpatterns = [
    path('', SeasonOrderView.as_view(), name='season_order_view'),
]