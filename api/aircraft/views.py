from django.http import Http404, response
from fleet.models import Aircraft, Airport, Flight
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import AircraftSerializer


class AircraftViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows aircraft to be viewed or created.
    """

    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer


class AircraftDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an aircraft instance.
    """

    serializer_class = AircraftSerializer
    queryset = Aircraft.objects.all()
