"""
Application order_details has one table in postgresql,
represented by OrderDetails Model.
"""

from django.db import models

from orders.models import Order
from CW_places.models import CWPlaces
from carwash_services.models import Services


class OrderDetail(models.Model):
    """Model for order_detail app. OrderDetails is in one to one dependancy
    with Order model from orders app - 'OneToOneField'.
    'order', 'service' and 'cawash_place' being fk's  are set to remove record
    if coresponding records in the other models are removed - 'on_delete' cascade.
    """
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    carwash_place = models.ForeignKey(CWPlaces, on_delete=models.CASCADE)
    price = models.FloatField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)

    class Meta:
        """Some data for the model.
         With managed True, Django will create the appropriate database tables in migrate or as part 
         of migrations and remove them as part of a flush management command.
         order and service fields combination should be unique - 'unique_together'.
        """
        managed = True
        db_table = 'order_detail'
        unique_together = (('service', 'order'),)

    def __str__(self):
        return f'Order:{self.order}, service: {self.service} '\
               f'place:{self.carwash_place}, price:{self.price} '\
               f'duration:{self.duration}, start time:{self.start_time}'
