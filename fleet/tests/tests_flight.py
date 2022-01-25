from django.http import response
from fleet.models import Flight, Aircraft, Airport
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


class FlightTests(APITestCase):
    """
    Test the Flight model and API
    """

    def setUp(self):
        """
        Set up test data
        """
        self.departure_airport = Airport.objects.create(
            icao="LGW", name="London Gatwick"
        )
        self.arrival_airport = Airport.objects.create(icao="JFK", name="New York JFK")
        self.aircraft = Aircraft.objects.create(
            serial_number="12345", manufacturer="Airbus"
        )
        self.flight = Flight.objects.create(
            aircraft=self.aircraft,
            departure_airport=self.departure_airport,
            arrival_airport=self.arrival_airport,
            departure_time="2022-02-10 10:30",
            arrival_time="2022-02-10 11:00",
        )

    def test_flight_create(self):
        """
        Test the Flight model can create a flight
        """
        data = {
            "aircraft": self.aircraft.id,
            "departure_airport": self.departure_airport.id,
            "arrival_airport": self.arrival_airport.id,
            "departure_time": "2022-02-11 10:30",
            "arrival_time": "2022-02-11 11:00",
        }
        url = reverse("flight")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Flight.objects.count(), 2)

    def test_flight_list(self):
        """
        Test the Flight model can list all flights
        """
        url = reverse("flight-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_departure_airport(self):
        """
        Test the Flight model can search for flights by departure airport
        """
        url = reverse("flight-list")
        response = self.client.get(
            url, {"departure_airport": self.departure_airport.icao}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_aircraft(self):
        """
        Test the Flight model can search for flights by aircraft
        """
        url = reverse("flight-list")
        response = self.client.get(
            url, {"aircraft": self.aircraft.serial_number}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
