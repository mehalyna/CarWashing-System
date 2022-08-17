from django.db import models

from car_washes.models import CarWashes


class Services(models.Model):
    service_name = models.CharField(
        max_length=50)
    service = models.IntegerField(
        primary_key=True,
        editable=False)

    def __str__(self):
        return f'Service name: {self.service_name}, Service: {self.service}'


class Carwash_Services(models.Model):
    carwash_service = models.OneToOneField(
        Services,
        on_delete=models.CASCADE,
        primary_key=True, )
    carwash = models.OneToOneField(
        CarWashes,
        on_delete=models.CASCADE,
        primary_key=True)

    def __str__(self):
        return f'Carwash service: {self.carwash_service}, Carwash: {self.carwash}'
