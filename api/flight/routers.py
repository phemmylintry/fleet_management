from django.urls import path

from .views import FlightListView, FlightView, FlightReportView

urlpatterns = [
    path("", FlightView.as_view(), name="flight"),
    path("list-flights", FlightListView.as_view(), name="flight-list"),
    path("report", FlightReportView.as_view(), name="flight-report"),
]
