from django.urls import path
from .views import WeatherDateView

urlpatterns = [
    path('', WeatherDateView.as_view(), name='weather_date_view'),
]