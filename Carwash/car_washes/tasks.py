import requests

from celery import shared_task


@shared_task
def set_car_wash_quantity_to_0(pk):
    """"
    Async task to set car wash quantity to 0
    """
    requests.put(
        f'http://127.0.0.1:8000/car_washes/{pk}/',
        data={'quantity_of_places': 0}
    )
