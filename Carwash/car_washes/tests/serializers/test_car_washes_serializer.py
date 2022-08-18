from django.test import TestCase

from car_washes.models import CarWashes
from car_washes.tests.factories import CarWashesFactory
from car_washes.serializers import CarWashesSerializer


class CarWashesSerializerTest(TestCase):
    
    def setUp(self):
        self.car_wash = CarWashesFactory()
    
    def test_instance_data(self):
        serializer = CarWashesSerializer(
            instance=self.car_wash
        )
        self.assertEqual(
            serializer.data['car_wash_name'],
            self.car_wash.car_wash_name
        )

        self.assertEqual(
            serializer.data['car_wash_address'],
            self.car_wash.car_wash_address
        )

        self.assertEqual(
            serializer.data['quantity_of_places'],
            self.car_wash.quantity_of_places
        )
    
    def test_validation(self):
        car_wash_data = {
            'car_wash_name': 'some name',
            'car_wash_address': 'some address',
            'quantity_of_places': 12
        }
        serializer = CarWashesSerializer(
            data=car_wash_data
        )
        self.assertTrue(serializer.is_valid())
