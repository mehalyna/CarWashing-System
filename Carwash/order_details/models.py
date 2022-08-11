from django.conf import settings
from django.db import models
from django.utils import timezone

from orders.models import Order
from carwash_places.models import CarwashPlaces
from services.models import Service


class OrderDetail(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    carwash_place = models.ForeignKey(CarwashPlaces, on_delete=models.CASCADE)
    price = models.FloatField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'order_detail'
        unique_together = (('service', 'order'),)

    def __str__(self):
        return f'order:{self.order}, service: {self.service}\
                , place:{self.carwash_place}, price:{self.price}\
                , duration:{self.duration}, start time:{self.start_time}'
