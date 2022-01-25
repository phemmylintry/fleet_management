from django.urls import path, include

from .aircraft.routers import urlpatterns as fleet_url
from .flight.routers import urlpatterns as flight_url
from .airport.routers import urlpatterns as airport_url

urlpatterns = [
    path('aircraft/', include(fleet_url)),
    path('flight/', include(flight_url)),
    path('airport/', include(airport_url)),
]