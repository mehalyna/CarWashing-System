import datetime
import factory
import factory.fuzzy
import random

from car_washes.models import CarWashes
from orders.models import Order
from users.models import Accounts, Users


class AccountFactory(factory.django.DjangoModelFactory):
    """
    Factory for account model. Generates random strings for email and password
    """

    email = factory.fuzzy.FuzzyText(
        length=15,
    )
    password = factory.fuzzy.FuzzyText(
        length=15,
    )

    class Meta:
        model = Accounts
        django_get_or_create = ('email',)


class UserFactory(factory.django.DjangoModelFactory):
    """
    Factory for user model. Generates random strings for email and password
    """
    
    phone_number = factory.fuzzy.FuzzyText(
        length=15,
    )
    full_name = factory.fuzzy.FuzzyText(
        length=100,
    )
    user_location = factory.fuzzy.FuzzyText(
        length=100,
    )
    account = factory.SubFactory(
        AccountFactory,
    )

    class Meta:
        model = Users
        django_get_or_create = ('phone_number',)


class CarWashFactory(factory.django.DjangoModelFactory):
    """
    Factory for car wash model. Generates random strings for email and password
    """
    
    car_wash_name = factory.fuzzy.FuzzyText(
        length=50,
    )
    car_wash_address = factory.fuzzy.FuzzyText(
        length=255,
    )
    quantity_of_places = factory.LazyAttribute(
        lambda _ :random.randint(0, 100)
    )

    class Meta:
        model = CarWashes


class OrderFactory(factory.django.DjangoModelFactory):
    """
    Factory for order model. Generates random strings for email and password
    """

    class Meta:
        model = Order
        django_get_or_create = ('user', 'car_wash')
    
    car_wash = factory.SubFactory(
        CarWashFactory,
    )
    user = factory.SubFactory(
        UserFactory,
    )
    order_current_status = factory.fuzzy.FuzzyText(
        length=Order.ORDER_CURRENT_STATUS_MAX_LENGTH - 3,
        prefix='New',
    )
    order_date_time = datetime.datetime.now()
    execution = datetime.datetime.now()
