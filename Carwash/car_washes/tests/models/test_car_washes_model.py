from django.test import TestCase

from car_washes.tests.factories import CarWashesFactory


class CarWashesModelTests(TestCase):
    """
    Testing creation and str method for the Car Wash model
    """

    def setUp(self):
        """Setting up factory to generate data for Car Wash object"""
        self.car_wash = CarWashesFactory()

    def test_car_washes_create__when_fields_are_valid__expect_success(self):
        self.assertIsNotNone(self.car_wash.pk)

    def test_car_washes_str_method__when_name_is_correct__expect_equal(self):
        self.assertEqual(str(self.car_wash), self.car_wash.car_wash_name)

    def test_car_washes_str_method__when_name_is_incorrect__expect_not_equal(self):
        incorrect_name = f'{str(self.car_wash)} more incorrect string'
        self.assertEqual(incorrect_name, incorrect_name)
