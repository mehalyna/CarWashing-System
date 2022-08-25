from django.db import models

# Create your models here.
class Places(models.Model):

    place_name = models.CharField(
        max_length=50
    )

    def __str__(self):
        return f'{self.place_name}'
