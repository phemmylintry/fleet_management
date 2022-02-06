from api.aircraft.serializers import AircraftSerializer
from api.airport.serializers import AirportSerializer
from django.utils import timezone
from fleet.models import Flight
from rest_framework import serializers


class BaseFlightSerializer(serializers.ModelSerializer):
    departure_time = serializers.DateTimeField(required=True)
    arrival_time = serializers.DateTimeField(required=True)

    class Meta:
        model = Flight
        fields = "__all__"

    def validate(self, attrs):
        departure_airport = attrs.get("departure_airport")
        arrival_airport = attrs.get("arrival_airport")
        departure_time = attrs.get("departure_time")
        arrival_time = attrs.get("arrival_time")

        # Check if departure and arrival airports are the same
        if departure_airport == arrival_airport:
            raise serializers.ValidationError(
                "Departure and arrival airports must be different"
            )

        # validate that departure time is not in the past
        if departure_time < timezone.now():
            raise serializers.ValidationError("Departure time cannot be in the past")

        # validate that arrival time is not in the past and is after departure time
        if arrival_time < timezone.now():
            raise serializers.ValidationError("Arrival time cannot be in the past")

        if arrival_time < departure_time:
            raise serializers.ValidationError(
                "Arrival time cannot be before departure time"
            )
        return attrs


class FlightSerializer(BaseFlightSerializer):
    """
    Flight model serializer
    """

    departure_time = serializers.DateTimeField(required=True)
    arrival_time = serializers.DateTimeField(required=True)
    departure_airport = serializers.SerializerMethodField()
    arrival_airport = serializers.SerializerMethodField()
    aircraft = serializers.SerializerMethodField()

    class Meta:
        model = Flight
        fields = "__all__"

    def get_departure_airport(self, obj):
        return AirportSerializer(obj.departure_airport).data

    def get_arrival_airport(self, obj):
        return AirportSerializer(obj.arrival_airport).data

    def get_aircraft(self, obj):
        return AircraftSerializer(obj.aircraft).data
