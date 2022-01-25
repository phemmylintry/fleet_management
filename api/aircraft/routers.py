from django.urls import path
from .views import AircraftViewSet, AircraftDetailViewSet

urlpatterns = [
    path('', AircraftViewSet.as_view(), name='aircraft'),
    path('<int:pk>', AircraftDetailViewSet.as_view(), name='aircraft-detail'),
]