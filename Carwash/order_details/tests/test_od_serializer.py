import factory

from django.test import TestCase

from order_details.serializer import OrderDetailSerializer
from order_details.tests.factories import OrderDetailFactory, OrderFactory, \
                                          ServiceFactory, CWPlacesFactory


class OrderDetailSerializerTest(TestCase):
    def test_instance_data(self):
        order = OrderFactory.create()
        service = ServiceFactory.create()
        CWPlace = CWPlacesFactory.create()
        orderdetail = OrderDetailFactory(order=order, service=service, carwash_place=CWPlace)
        serializer = OrderDetailSerializer(instance=orderdetail)

        self.assertEqual(serializer.data['price'], orderdetail.price)
        self.assertEqual(serializer.data['duration'], orderdetail.duration)
        self.assertEqual(serializer.data['start_time'], orderdetail.start_time)
        self.assertEqual(serializer.data['service'], service.pk)
        self.assertEqual(serializer.data['order'], order.pk)
        self.assertEqual(serializer.data['carwash_place'], CWPlace.pk)
