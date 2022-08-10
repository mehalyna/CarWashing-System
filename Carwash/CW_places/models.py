from django.db import models
from car_washes.models import CarWashes
from places.models import Places


class CWPlaces(models.Model):
    carwash_place = models.IntegerField(primary_key=True, editable=False)
    place = models.ForeignKey(Places, on_delete=models.CASCADE, null=True)
    carwash = models.ForeignKey(Carwashes, on_delete=models.CASCADE, null=True)
    is_free = models.BooleanField(default=False)

    def __str__(self):
        return self.carwash_place_id, self.is_free
