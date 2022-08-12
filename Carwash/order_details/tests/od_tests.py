import unittest
from unittest import TestCase

from order_details.tests.factories import *
from order_details.models import OrderDetail


class OrderDetailTestCase(TestCase):

    def setUp(self) -> None:
        self.user = UsersFactory()
        self.place = CarwashPlacesFactory()
        self.carwash = CarWashesFactory()
        self.service = ServiceFactory()
        self.order = OrderFactory(car_wash=self.carwash, user=self.user)
        self.CWPlace = CWPlacesFactory(place_id=self.place, carwash_id=self.carwash)
        self.order_detail = OrderDetailFactory(order=self.order,
                                               service=self.service,
                                               carwash_place=self.place)

    def test_crud_orderdetail(self):
        self.order_detail.create()
        self.assertEqual(len(OrderDetail.objects.all()), 1)


if __name__ == '__main__':
    unittest.main()
