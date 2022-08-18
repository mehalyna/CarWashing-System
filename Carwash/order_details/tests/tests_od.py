import datetime

from django.test import TestCase

from order_details.tests.factories import AccountsFactory, UsersFactory, \
                                          PlacesFactory, CarWashesFactory, \
                                          ServiceFactory, OrderFactory, \
                                          CWPlacesFactory, OrderDetailFactory

from order_details.models import OrderDetail


class OrderDetailTestCase(TestCase):

    def setUp(self) -> None:
        self.account = AccountsFactory()
        self.user = UsersFactory(account=self.account)
        self.place = PlacesFactory()
        self.carwash = CarWashesFactory()
        self.service = ServiceFactory()
        self.order = OrderFactory(car_wash=self.carwash, user=self.user)
        self.CWPlace = CWPlacesFactory(place=self.place, carwash=self.carwash)

    def test_crud_orderdetail(self):

        OrderDetailFactory(order=self.order,
                           service=self.service,
                           carwash_place=self.CWPlace,
                           price=10.5,
                           duration=15,
                           start_time=datetime.time(18, 0, 0))

        self.assertTrue(OrderDetail.objects.get(price=10.5))
        self.assertTrue(OrderDetail.objects.get(duration=15))
        self.assertTrue(OrderDetail.objects.get(start_time=datetime.time(18, 0, 0)))
        self.assertEqual(len(OrderDetail.objects.all()), 1)
        od = OrderDetail.objects.filter(price=10.5)
        od.update(price=20)
        self.assertTrue(OrderDetail.objects.get(price=20))
        self.assertEqual(len(OrderDetail.objects.all()), 1)
        OrderDetail.objects.filter(pk=1).delete()
        self.assertEqual(len(OrderDetail.objects.all()), 1)

    def test_create_multiple_entries_for_orderdetails(self):
        OrderDetailFactory.create_batch(10)
        self.assertEqual(len(OrderDetail.objects.all()), 10)

    def test_unique_together_for_services_and_orders(self):
        od1 = OrderDetailFactory(service=self.service, order=self.order)
        od2 = OrderDetailFactory(service=self.service, order=self.order)
        self.assertEqual(od1, od2)
        self.assertEqual(len(OrderDetail.objects.all()), 1)
        OrderDetailFactory(service=self.service, carwash_place=self.CWPlace)
        OrderDetailFactory(service=self.service, carwash_place=self.CWPlace)
        self.assertEqual(len(OrderDetail.objects.all()), 3)
