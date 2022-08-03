from django.conf import settings
from django.db import models
from django.utils import timezone


class OrderDetails(models.Model):
    service = models.OneToOneField('Services', models.DO_NOTHING, primary_key=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    price = models.FloatField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    carwash_place = models.ForeignKey('CarwashPlaces', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'order_details'
        unique_together = (('service', 'order'),)
