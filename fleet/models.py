from django.db import models


class Aircraft(models.Model):
    """
    Aircraft model
    """

    serial_number = models.CharField(
        max_length=512, unique=True, null=True, blank=True, default=None
    )
    manufacturer = models.CharField(max_length=512, default=None, null=True, blank=True)

    def __str__(self):
        return self.serial_number


class Airport(models.Model):
    """
    Airport model
    """

    icao_code = models.CharField(
        max_length=4, unique=True, default=None, null=True, blank=True
    )

    def __str__(self):
        return self.icao_code


class Flight(models.Model):
    """
    Flight model
    """

    aircraft = models.ForeignKey(
        Aircraft, on_delete=models.CASCADE, default=None, null=True, blank=True, related_name="flights"
    )
    departure_airport = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
        related_name="departure_airport",
    )
    arrival_airport = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
        related_name="arrival_airport",
    )
    departure_time = models.DateTimeField(default=None, null=True, blank=True)
    arrival_time = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return self.aircraft.icao_code
