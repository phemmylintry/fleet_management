from django.urls import path
from .views import AircraftViewSet, AircraftDetailViewSet

urlpatterns = [
    path('aircraft/', AircraftViewSet.as_view(), name='aircraft'),
    path('aircraft/<int:pk>/', AircraftDetailViewSet.as_view(), name='aircraft-detail'),
]