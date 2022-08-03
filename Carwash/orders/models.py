from django.db import models

from car_washes.models import CarWashes
from users.models import Users


class Order(models.Model):

    ORDER_CURRENT_STATUS_MAX_LENGTH = 20

    car_wash_id = models.ForeignKey(
        CarWashes,
        on_delete=models.CASCADE,
        )

    user_id = models.ForeignKey(
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
