from django.db import models

# from Carwash.car_washes.models import CarWashes


class CWPlaces(models.Model):
    carwash_place_id = models.IntegerField(primary_key=True, editable=False)
    place_id = models.ForeignKey('Places', on_delete=models.CASCADE, null=True)
    carwash_id = models.ForeignKey('CarWashes', on_delete=models.CASCADE, null=True)
    is_free = models.BooleanField(default=False)

    def __str__(self):
        return self.carwash_place_id, self.is_free
