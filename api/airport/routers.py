from django.urls import path
from .views import AirportView, AirportDetailView


urlpatterns = [
    path('', AirportView.as_view(), name='airport'),
    path('<int:pk>', AirportDetailView.as_view(), name='airport-detail'),
]