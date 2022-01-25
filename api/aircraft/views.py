from django.http import Http404, response
from fleet.models import Aircraft, Airport, Flight
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AircraftSerializer


class AircraftViewSet(APIView):
    """
    API endpoint that allows aircraft to be viewed or created.
    """

    def get(self, request, format=None):
        response = {
            "status": 1,
            "message": "Successfully retrieved aircraft list.",
            "data": "",
        }
        aircraft = Aircraft.objects.all()
        serializer = AircraftSerializer(aircraft, many=True)
        response["data"] = serializer.data
        return Response(response)

    def post(self, request, format=None):
        response = {
            "status": 1,
            "message": "Successfully created new aircraft.",
            "data": "",
        }
        serializer = AircraftSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
        except Exception as e:
            return Response({"error": str(e)}, status=400)

        response["data"] = serializer.data
        return Response(response, status=201)


class AircraftDetailViewSet(APIView):
    """
    Retrieve, update or delete an aircraft instance.
    """

    def get_object(self, pk):
        try:
            return Aircraft.objects.get(pk=pk)
        except Aircraft.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        aircraft = self.get_object(pk)
        serializer = AircraftSerializer(aircraft)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        aircraft = self.get_object(pk)
        serializer = AircraftSerializer(aircraft, data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
        except Exception as e:
            return Response({"error": str(e)}, status=400)

        return Response(serializer.data, status=200)

    def delete(self, request, pk, format=None):
        aircraft = self.get_object(pk)
        aircraft.delete()
        return Response(status=204)
