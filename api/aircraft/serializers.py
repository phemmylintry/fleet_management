from rest_framework import serializers
from fleet.models import Aircraft, Airport, Flight


class AircraftSerializer(serializers.ModelSerializer):
    """
    Aircraft model serializer
    """

    class Meta:
        model = Aircraft
        fields = ("id", "serial_number", "manufacturer")
