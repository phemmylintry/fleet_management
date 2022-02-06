from api.aircraft.serializers import AircraftSerializer
from django.db.models import Q
from django.http import Http404
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from fleet.models import Flight
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import FlightFilter
from .serializers import BaseFlightSerializer, FlightSerializer


class FlightView(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = FlightFilter
    serializer_class = BaseFlightSerializer


class FlightDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BaseFlightSerializer
    queryset = Flight.objects.all()


class FlightReportView(APIView):
    serializer_class = FlightSerializer

    def get(self, request, format=None):
        response = {
            "status": 1,
            "message": "Successfully retrieved flights",
            "data": {},
        }
        departure_time = request.query_params.get("departure_time", None)
        arrival_time = request.query_params.get("arrival_time", None)

        try:
            queryset = (
                Flight.objects.select_related("aircraft", "departure_airport")
                .filter(
                    Q(departure_time__gte=departure_time)
                    & Q(arrival_time__lte=arrival_time)
                )
                .order_by("departure_airport")
            )
        except ValueError:
            return Response(
                "Invalid query parameters", status=status.HTTP_400_BAD_REQUEST
            )
        data = {}
        for flight in queryset:
            if not data.__contains__(flight.departure_airport.icao):
                flight_time_for_each_aircraft = []
                data[flight.departure_airport.icao] = {
                    "airport_name": flight.departure_airport.name,
                    "flights_count": 0,
                    "flight_time_for_each_aircraft": flight_time_for_each_aircraft,
                }
            data[flight.departure_airport.icao]["flights_count"] += 1
            flight_time_for_each_aircraft.append(
                {
                    "aircraft": AircraftSerializer(flight.aircraft).data,
                    "flight_time": "{} minutes".format(
                        (flight.arrival_time - flight.departure_time).total_seconds()
                        / 60
                    ),
                }
            )

        response["data"] = data
        return Response(response)
