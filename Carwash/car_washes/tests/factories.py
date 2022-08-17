import factory
from faker import Faker

from car_washes.models import CarWashes


faker = Faker()

class CarWashesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CarWashes
    
    car_wash_name = factory.LazyAttribute(lambda _: faker.name())
    car_wash_address = factory.LazyAttribute(lambda _: faker.address())
    quantity_of_places = factory.LazyAttribute(lambda _: faker.random_int())