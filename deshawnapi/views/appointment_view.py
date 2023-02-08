from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from deshawnapi.models import Appointment, Walker


class AppointmentView(ViewSet):
#if we are defining something in the class, we call it a 'method' defining a method on the class
#when defining inside a class specifically
    def retrieve(self, request, pk=None): #defining a method on the class that accepts the parsed path, a request and primary key
        appointment = Appointment.objects.get(pk=pk) #gets a single appointment instance of the Appointment database model class declaring that appointment variable and assigning to the appointment object that matches PK
        serialized = AppointmentSerializer(appointment, context={'request': request}) #declaring the variable serialized and assigning it's value to the return value of the appointment serializer using the appointment object defined above
        return Response(serialized.data, status=status.HTTP_200_OK)

#in a function definition in the parenthesis, we call those parameters (line 16) (line 18 has arguments)

    def list(self, request): #defining a method list on the class with parameters self and a request
        appointments = Appointment.objects.all() #we are declaring the appointments variable and assigning it the value of a list of instances of the Appointment database model, queries the Appointment table in the database to return a list of instances of the Appointment database model
        serialized = AppointmentSerializer(appointments, many=True) #declaring the serialized variable  and assigning it to the return JSON string of the appointment serializer which takes the arguments of appointments and Many=true, which tells the return to expect a list of instances
        return Response(serialized.data, status=status.HTTP_200_OK) #returns the body of a JSON stringified object to the client and a status code of 200 OK in the headers

    def create(self, request):
        # Get the related walker from the database using the request body value
        client_walker_id = request.data["walkerId"]
        walker_instance = Walker.objects.get(pk=client_walker_id)

        # Create a new appointment instance
        appointment = Appointment()

        # Use Walker instance as the value of the model property
        appointment.walker = walker_instance

        # Assign the appointment date using the request body value
        appointment.date = request.data["date"]

        # Performs the INSERT statement into the deshawnapi_appointment table
        appointment.save()

        # Serialization will be covered in the next chapter
        serialized = AppointmentSerializer(appointment, many=False)

        # Respond with the newly created appointment in JSON format with a 201 status code
        return Response(serialized.data, status=status.HTTP_201_CREATED)


# The serializer will be covered in the next chapter
class AppointmentSerializer(serializers.ModelSerializer):
#JSON stringifies an object based on the fields we define
    class Meta:
        model = Appointment
        fields = ('id', 'walker', 'date',)
    #why did we define these fields: because we want to return the id, walker, an date of the appointment from this tuple as that is what the client is expecting