import factory

from factory import fuzzy
from faker import Faker
from django.test import TestCase
from car_washes.models import CarWashes
from CW_places.serializers import CWPlacesSerializer
from CW_places.models import CWPlaces
from places.models import Places


fake = Faker()


class PlacesFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Places

    cwplaces = 1
    place_name = 2


class CarWashesFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = CarWashes

    car_wash_name = fuzzy.FuzzyAttribute(lambda: f'{fake.name()} wash')
    car_wash_address = fake.address()
    quantity_of_places = fuzzy.FuzzyInteger(1, 100)


class CWPlacesFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = CWPlaces

    carwash_place = 10
    place = factory.SubFactory(PlacesFactory)
    carwash = factory.SubFactory(CarWashesFactory)
    is_free = fuzzy.FuzzyChoice(choices=(True, True, True, True, False,))


class CWPlacesSerializerTest(TestCase):

    def setUp(self):
        self.cw_places = CWPlacesFactory()
        self.places = PlacesFactory()
        self.carwashes = CarWashesFactory()

    def test_if_data_instantiate_correct(self):
        serializer = CWPlacesSerializer(instance=self.cw_places)
        self.assertEqual(serializer.data['carwash_place'], self.cw_places.carwash_place)
        self.assertEqual(serializer.data['is_free'], self.cw_places.is_free)
        self.assertEqual(serializer.data['place'], self.cw_places.place.place_name)
        self.assertEqual(serializer.data['carwash'], self.cw_places.carwash.id)

