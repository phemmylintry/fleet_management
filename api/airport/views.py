from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from fleet.models import Airport
from .serializers import AirportSerializer


class AirportView(generics.ListCreateAPIView):
    """
    API endpoint that allows airports to be viewed or created.
    """

    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class AirportDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an airport instance.
    """

    seriaizer_class = AirportSerializer
    queryset = Airport.objects.all()
