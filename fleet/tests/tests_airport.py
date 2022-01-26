from django.http import response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from fleet.models import Airport


class AirportTests(APITestCase):
    """
    Test the Airport model and API
    """

    def setUp(self):
        """
        Set up test data
        """
        self.airport = Airport.objects.create(
            icao="LHR", name="London Heathrow"
        )
    
    def test_airport_create(self):
        """
        Test that an Airport can be created
        """
        url = reverse("airport")
        response = self.client.post(url, {"icao": "LHRA", "name": "London Heathrow"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_airport_create_fail(self):
        url = reverse("airport")
        response = self.client.post(url, {"icao": "LHR", "name": "London Heathrow"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    