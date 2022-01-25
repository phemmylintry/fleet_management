from django.urls import reverse
from fleet.models import Aircraft
from rest_framework import status
from rest_framework.test import APITestCase
from .factories import AircraftFactory, AirportFactory, FlightFactory


class AircraftTests(APITestCase):
    """
    Test the Aircraft model and API
    """

    def setUp(self):
        """
        Set up test data
        """
        self.aircraft = AircraftFactory.create_batch(5)
        for i in self.aircraft:
            print(i)

    def test_aircraft_create(self):
        """
        Test the Aircraft model can create an aircraft
        """
        url = reverse("aircraft")
        response = self.client.post(
            url, {"serial_number": "12346", "manufacturer": "Airbus"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Aircraft.objects.count(), 2)

    def test_aircraft_list(self):
        """
        Test the Aircraft model can list all aircraft
        """
        url = reverse("aircraft")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_aircraft_detail(self):
        """
        Test the Aircraft model can update an aircraft
        """
        url = reverse("aircraft-detail", args=[self.aircraft.id])
        response = self.client.put( url, {"manufacturer": "Boeing"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Aircraft.objects.get(id=self.aircraft.id).manufacturer, "Boeing")
