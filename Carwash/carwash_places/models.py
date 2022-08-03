from django.db import models

# Create your models here.

class CarwashPlaces(models.Model):

    place_id = models.CharField(
        max_length=10,
        unique=True
    )
    place_name = models.CharField(
        max_length=50
    )

