from django.db import models

from car_washes.models import CarWashes
from places.models import Places



class CWPlaces(models.Model):

class TimeStampedModel(models.Model):
    """Additional class to add extra functionality to the main class"""
    added = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CWPlaces(TimeStampedModel):

    """Main model class"""
    carwash_place = models.IntegerField(primary_key=True)
    place = models.ForeignKey(Places, on_delete=models.CASCADE, null=True)
    carwash = models.ForeignKey(CarWashes, on_delete=models.CASCADE, null=True)
    is_free = models.BooleanField(default=False)
    confirmed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Carwash Id -> {self.carwash_place}, free -> {self.is_free}'


