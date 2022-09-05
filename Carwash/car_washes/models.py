from django.db import models


class CarWashes(models.Model):
    """
    Car Wash Model
    columns:
        car_wash_name: character varying
        car_wash_address: character varying
        quantity_of_cars: integer
    """
    car_wash_name = models.CharField(max_length=50)
    car_wash_address = models.CharField(max_length=255)
    quantity_of_places = models.IntegerField()

    def __str__(self):
        """Return car wash name"""
        return f'{self.car_wash_name}'
