from fleet.models import Airport
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class AirportSerializer(serializers.ModelSerializer):
    icao = serializers.CharField(
        max_length=4,
        required=True,
        validators=[UniqueValidator(queryset=Airport.objects.all())],
    )

    class Meta:
        model = Airport
        fields = "__all__"

    def validate(self, attrs):
        icao = attrs.get("icao")

        if len(icao) != 4:
            raise serializers.ValidationError("ICAO must be 4 characters long")

        return attrs
