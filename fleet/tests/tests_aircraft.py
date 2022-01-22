from django.http import response
from django.urls import reverse
from fleet.models import Aircraft
from rest_framework import status
from rest_framework.test import APITestCase


class AircraftTests(APITestCase):
    """
    Test the Aircraft model and API
    """

    def setUp(self):
        """
        Set up test data
        """
        self.aircraft = Aircraft.objects.create(
            serial_number='12345', manufacturer='Airbus')

    def test_aircraft_create(self):
        """
        Test the Aircraft model can create an aircraft
        """
        self.assertEqual(self.aircraft.serial_number, '12345')
        self.assertEqual(self.aircraft.manufacturer, 'Airbus')

    def test_aircraft_list(self):
        """
        Test the Aircraft model can list all aircraft
        """
        url = reverse('aircraft')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)\
    
    def test_aircraft_detail(self):
        """
        Test the Aircraft model can retrieve an aircraft
        """
        url = reverse('aircraft-detail', args=[self.aircraft.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)