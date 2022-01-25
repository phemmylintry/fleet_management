import imp
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from fleet.models import Airport
from .serializers import AirportSerializer


class AirportView(APIView):
    """
    API endpoint that allows airports to be viewed or created.
    """

    def get(self, request):
        """
        Return a list of all airports.
        """
        airports = Airport.objects.all()
        serializer = AirportSerializer(airports, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new airport.
        """
        serializer = AirportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AirportDetailView(APIView):
    """
    Retrieve, update or delete an airport instance.
    """

    def get_object(self, pk):
        try:
            return Airport.objects.get(pk=pk)
        except Airport.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        airport = self.get_object(pk)
        serializer = AirportSerializer(airport)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        airport = self.get_object(pk)
        serializer = AirportSerializer(airport, data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
        except Exception as e:
            return Response({"error": str(e)}, status=400)

        return Response(serializer.data, status=200)

    def delete(self, request, pk, format=None):
        airport = self.get_object(pk)
        airport.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)