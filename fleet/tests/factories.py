import factory
from fleet.models import Aircraft, Flight, Airport


class AircraftFactory(factory.Factory):
    class Meta:
        model = Aircraft

    serial_number = factory.Faker("pystr", max_chars=5)
    manufacturer = factory.Faker("company")


class AirportFactory(factory.Factory):
    class Meta:
        model = Airport

    name = factory.Faker("city")
    icao = factory.Faker("pystr", max_chars=4)


class FlightFactory(factory.Factory):
    class Meta:
        model = Flight

    aircraft = factory.SubFactory(AircraftFactory)
    departure_airport = factory.SubFactory(AirportFactory)
    arrival_airport = factory.SubFactory(AirportFactory)
    departure_time = factory.Faker(
        "date_time_between", start_date="-1y", end_date="+1y"
    )
    arrival_time = factory.Faker("date_time_between", start_date="-1y", end_date="+1y")
