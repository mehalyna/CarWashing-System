from django.db import models

from car_washes.models import CarWashes
from users.models import Users


class Order(models.Model):
    """
    Model to store orders. 
    Foreign key to CarWashes model.
    Foreign key to Users model.
    """

    ORDER_CURRENT_STATUS_MAX_LENGTH = 20

    car_wash = models.ForeignKey(
        CarWashes,
        on_delete=models.CASCADE,
        )

    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
    )

    order_current_status = models.CharField(
        max_length=ORDER_CURRENT_STATUS_MAX_LENGTH,
    )

    order_date_time = models.DateTimeField(
        auto_now_add=True,
    )

    execution = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f'Order Date: {self.order_date_time}, '\
               f'Status: {self.order_current_status}'
