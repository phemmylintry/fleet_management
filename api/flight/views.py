from django.http import Http404
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from fleet.models import Flight
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import FlightFilter
from .serializers import FlightSerializer


class FlightView(APIView):
    serializer_class = FlightSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = FlightFilter


class FlightDetailView(APIView):
    serializer_class = FlightSerializer

    def get_object(self, pk):
        try:
            return Flight.objects.get(pk=pk)
        except Flight.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        flight = self.get_object(pk)
        serializer = self.serializer_class(flight)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        flight = self.get_object(pk)
        serializer = self.serializer_class(flight, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        flight = self.get_object(pk)
        flight.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FlightReportView(APIView):
    serializer_class = FlightSerializer

    def get(self, request, format=None):
        response = {'status':1, 'message':'Successfully retrieved flights', 'data':{}}
        departure_time = request.query_params.get("departure_time", None)
        arrival_time = request.query_params.get("arrival_time", None)
        current_time = timezone.now()

        try:
            queryset = Flight.objects.select_related(
                "aircraft", "departure_airport"
            ).filter(departure_time__gte=departure_time, arrival_time__lte=arrival_time)
        except ValueError:
            return Response(
                "Invalid query parameters", status=status.HTTP_400_BAD_REQUEST
            )

        data = []
        for flight in queryset: 
            number_of_flights = flight.departure_airport.departure_flights.all()
            data.append(
                {
                    "airport" : {
                        "id" : flight.departure_airport.id,
                        "icao" : flight.departure_airport.icao,
                        "number_of_flights" : len(number_of_flights)
                    },
                    # "in-flight-time-per-aricraft" : [{
                    #     "serial_number" : aircraft.serial_number,
                    #     "in_flight_time" : aircraft.in_flight_time,
                    # } for aircraft in aircrafts]
                }
            )
        response['data'] = data
        return Response(response)
