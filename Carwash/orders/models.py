from django.db import models

from car_washes.models import CarWashes
from users.models import Users


class Order(models.Model):
    """
    Model to store orders. 

    Attributes

        car_wash: int
            foreign key to CarWashes model

        user: int
            foreign key to Users model

        order_current_stats: str
            The current status of the order(New, In progress, Complete, etc.)

        order_date_time: datetime
            The date and time when the order is placed
        
        execution: datetime
            Date and time when order has started (In progress status)
        
        ORDER_CURRENT_STATUS_MAX_LENGTH: int
            Maximum length of order current status

    Methods

        __str__
            Override for better and more meaningful representation of instance
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
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Order Date: {self.order_date_time}, '\
               f'Status: {self.order_current_status}'
