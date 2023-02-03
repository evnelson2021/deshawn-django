
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from deshawnapi.models import City


class CityView(ViewSet):

    def retrieve(self, request, pk=None):
        # Step 1: Get a single city based on the primary key in the request URL
        city = City.objects.get(pk=pk)

        # Step 2: Serialize the city record as JSON
        serialized = CitySerializer(city, context={'request': request})

        # Step 3: Send JSON response to client with 200 status code
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        # Step 1: Get all city data from the database
        cities = City.objects.all()

        # Step 2: Convert the data to JSON format
        serialized = CitySerializer(cities, many=True)

        # Step 3: Respond to the client with the JSON data and 200 status code
        return Response(serialized.data, status=status.HTTP_200_OK)

    # Serialization - The process of converting a data structure into a format that can be stored or transmitted (e.g. over the WWW) and reconstructed later. When the information is retrieved later using the same formatting mechanism, the original object is created again for use by your code.

class CitySerializer(serializers.ModelSerializer):
    # subclass of Meta
    class Meta:
        # specifies which model you want to use
        model = City
        # specifies which fields in that model should be in the final JSON string
        fields = ('id', 'name',)

