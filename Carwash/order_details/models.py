from django.db import models

from orders.models import Order
from CW_places.models import CWPlaces
from carwash_services.models import Services


class OrderDetail(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    carwash_place = models.ForeignKey(CWPlaces, on_delete=models.CASCADE)
    price = models.FloatField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'order_detail'
        unique_together = (('service', 'order'),)

    def __str__(self):
        return f'Order:{self.order}, service: {self.service} '\
               f'place:{self.carwash_place}, price:{self.price} '\
               f'duration:{self.duration}, start time:{self.start_time}'
