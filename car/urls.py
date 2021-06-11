from django.urls import path, include
from car.views import car_view


urlpatterns = [
    path("car/", car_view),
    path("car/<int:id>", car_view),
]
