import django_filters
from fleet.models import Flight


class FlightFilter(django_filters.FilterSet):
    departure_airport = django_filters.CharFilter(field_name="departure_airport__icao")
    arrival_airport = django_filters.CharFilter(field_name="arrival_airport__icao")
    aircraft = django_filters.CharFilter(field_name="aircraft__serial_number")
    departure_time_gte = django_filters.DateTimeFilter(
        field_name="departure_time", lookup_expr="gte"
    )
    departure_time_lte = django_filters.DateTimeFilter(
        field_name="departure_time", lookup_expr="lte"
    )

    class Meta:
        model = Flight
        fields = (
            "aircraft",
            "departure_airport",
            "arrival_airport",
            "departure_time_gte",
            "departure_time_lte",
        )
