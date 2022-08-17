import factory
from faker import Faker

from CW_places.models import CWPlaces

from car_washes.models import CarWashes
from places.models import Places

faker = Faker()


class CWPlacesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CWPlaces
    
    carwash_place = factory.LazyAttribute(lambda _: faker.random_int())
    place = Place()
    carwash = CarWashes()
    is_free = factory.LazyAttribute(lambda _: faker.boolean())
