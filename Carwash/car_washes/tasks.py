from celery import shared_task

from car_washes.models import CarWashes


@shared_task
def set_car_wash_quantity_to_0(pk):
    car_wash = CarWashes.objects.get(pk=pk)
    car_wash.quantity_of_places = 0
    car_wash.save()
