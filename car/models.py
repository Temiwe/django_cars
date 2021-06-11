from django.db import models


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    vin_number = models.CharField(max_length=100)
    car_color = models.ForeignKey("CarColor", on_delete=models.SET_NULL, null=True)
    car_model = models.ForeignKey("CarModel", on_delete=models.SET_NULL, null=True)
    car_date = models.ForeignKey("CarDate", on_delete=models.SET_NULL, null=True)
    car_type = models.ForeignKey("CarType", on_delete=models.SET_NULL, null=True)

    def company(self):
        return self.car_model.company

    def carcolor(self):
        return self.car_color.name

    def cardate(self):
        return self.car_date.name

    def cartype(self):
        return self.car_type.name


    def __str__(self):
        return f"Name: {self.name} vin_number: {self.vin_number}"


class CarModel(models.Model):

    name = models.CharField(max_length=100)
    company = models.ForeignKey("car.Company", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Company(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"


class CarColor(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CarDate(models.Model):

    name = models.CharField(max_length=4, default='1950')

    def __str__(self):
        return self.name


class CarType(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
