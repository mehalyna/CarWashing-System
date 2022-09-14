from django.db import models


class CarWashes(models.Model):
    """
    Car Wash Model
    columns:
        car_wash_name: name of the car wash
        car_wash_address: address of the car wash
        quantity_of_cars: quantity of cars in the car wash
    """
    car_wash_name = models.CharField(max_length=50)
    car_wash_address = models.CharField(max_length=255)
    quantity_of_places = models.IntegerField()

    def __str__(self):
        return f'{self.car_wash_name}'
