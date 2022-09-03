from __future__ import absolute_import

from django.test.client import RequestFactory
from django.contrib import admin

from celery import shared_task

from car_washes.models import CarWashes


@shared_task
def car_wash_task(pk_of_model):
    queryset = CarWashes.objects.filter(pk=pk_of_model)

    rf = RequestFactory()

    request = rf.put('/car_washes/{}/'.format(pk_of_model)
                     , data={'quantity_of_places': 0}
                     , content_type='application/json')

    admin.site._registry[CarWashes].change_view(request, pk_of_model, data={'quantity_of_places': 0})
