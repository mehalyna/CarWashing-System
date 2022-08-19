import factory

from factory import fuzzy
from faker import Faker
from car_washes.models import CarWashes
from CW_places.models import CWPlaces
from places.models import Places
from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()
fake = Faker()


class PlacesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Places

    cwplaces = 1
    place_name = 1


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


class CwPlacesModelTest(TestCase):
    def setUp(self):
        self.carwash_place = 1
        self.place = PlacesFactory()
        self.carwash = CarWashesFactory()
        self.test_model = CWPlaces.objects.create(carwash_place=self.carwash_place,
                                                  place=self.place,
                                                  carwash=self.carwash,
                                                  )

    def test_create_cw_places_model(self):
        assert isinstance(self.test_model, CWPlaces)


class UserTest(TestCase):
    def setUp(self):
        self.email = "testuser@abv.bg"
        self.password = "z"
        self.test_user = User.objects.create_user(
            email=self.email,
            password=self.password,
        )

    def test_create_user(self):
        assert isinstance(self.test_user, User)

    def test_default_user_is_active(self):
        assert self.test_user.is_active

    def test_default_user_is_staff(self):
        assert not self.test_user.is_staff

    def test_default_user_is_superuser(self):
        assert not self.test_user.is_superuser
