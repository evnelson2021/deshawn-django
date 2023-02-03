from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from deshawnapi.views import WalkerView, CityView, DogView, AppointmentView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'walkers', WalkerView, 'walk')
router.register(r'cities', CityView, 'city')
router.register(r'dogs', DogView, 'dog')
router.register(r'appointments', AppointmentView, 'appointment')
# The first argument is what you want your URL path to be. The second argument is the view that will handle client requests to that route. The third argument is needed in order for a route to be registered, but it is unused in our API and will not be covered or discussed.

urlpatterns = [
    path('', include(router.urls)),
]

