from django.urls import path

from .views import FlightDetailView, FlightReportView, FlightView

urlpatterns = [
    path("", FlightView.as_view(), name="flight"),
    path("<int:pk>", FlightDetailView.as_view(), name="flight-detail"),
    path("report", FlightReportView.as_view(), name="flight-report"),
]
