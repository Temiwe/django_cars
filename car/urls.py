from django.urls import path, include
from car.views import CarListView, CarDetailView, car_create, CarModelListView, CarModelDetailView, carmodel_create, CompanyListView, CompanyDetailView, company_create

urlpatterns = [
    path("car/", CarListView.as_view(), name="car-list"),
    path("models/", CarModelListView.as_view(), name="car-models"),
    path("models/<int:pk>", CarModelDetailView.as_view(), name="car-models-detail"),
    path("models/create", carmodel_create, name="carmodel-create"),
    path("car/create", car_create, name="car-create"),
    path("car/<int:pk>", CarDetailView.as_view(), name="car-detail"),
    path("companies/", CompanyListView.as_view(), name="company-list"),
    path("companies/<int:pk>", CompanyDetailView.as_view(), name="company-detail"),
    path("companies/create", company_create, name="company-create"),
]
