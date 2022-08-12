import datetime

import factory

from factory import Faker, fuzzy

from order_details.models import OrderDetail
from orders.models import Order
from services.models import Service
from carwash_places.models import CarwashPlaces
from CW_places.models import CWPlaces
from car_washes.models import CarWashes
from users.models import Users


class UsersFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Users
        django_get_or_create = ('account')

    phone_number = Faker("phone_nubmer")
    full_name = Faker("full_name")
    user_location = Faker("address")
    account = factory.post_generation(lambda obj: obj)


class CarwashPlacesFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = CarwashPlaces
        django_get_or_create = ('place_id')

    place_id = factory.Sequence(lambda n: n)
    place_name = factory.Sequence(lambda p: f'place_{p}')


class CarWashesFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = CarWashes
        django_get_or_create = ('car_wash_name')

    car_wash_name = fuzzy.FuzzyAttribute(lambda n: f'{Faker("name")} wash')
    car_wash_address = Faker("address")
    quantity_of_places = fuzzy.FuzzyInteger(1, 100)


class ServiceFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Service
        django_get_or_create = ('name')

    name = Faker("name")


class OrderFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Order
        django_get_or_create = ('car_wash', 'user')

    car_wash = Faker("name")
    user = factory.SubFactory(UsersFactory)
    order_current_status = fuzzy.FuzzyChoice(choices=['Cancelled', 'Ready'] + ['Confirmed']*10)
    order_date_time = fuzzy.FuzzyDateTime(datetime.datetime.now())
    execution = fuzzy.FuzzyDateTime(datetime.datetime.now())


class CWPlacesFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = CWPlaces
        django_get_or_create = ('place_id, carwash_id')

    carwash_place_id = factory.Sequence(lambda n: n)
    place_id = factory.SubFactory(CarwashPlacesFactory)
    carwash_id = factory.SubFactory(CarWashesFactory)
    is_free = fuzzy.FuzzyChoice(choices=(True, True, True, True, False,))


class OrderDetailFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = OrderDetail
        django_get_or_create = ('order', 'service', 'carwash_place',
                                'price', 'duration', 'start_time')

    order = factory.SubFactory(OrderFactory)
    service = factory.SubFactory(ServiceFactory)
    carwash_place = factory.SubFactory(CarwashPlacesFactory)
    price = fuzzy.FuzzyFloat(1, 1000)
    duration = fuzzy.FuzzyInteger(1, 720)
    start_time = fuzzy.FuzzyDateTime(datetime.datetime.now())
