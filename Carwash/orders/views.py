from rest_framework.viewsets import ModelViewSet

from car_washes.models import CarWashes
from orders.models import Order
from orders.serializers import OrderSerializer
from users.models import Accounts, Users


class OrderView(ModelViewSet):
    """
    Order model view set

    Attributes
        queryset: collection of all Order objects/rows in database
        serializer_class: reference to OrderSerializer

    Methods

        retrieve: self, request, *args, **kwargs
            Override to alter returned 
            information of foreign keys in JSON response

    Private methods

        _alter_user_information: self, data
            returns the user information in a python dictionary

        _alter_car_wash_information: self, data
            returns the car_wash information in a python dictionary
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def _alter_user_information(self, data: serializer_class) -> dict:
        """Add full user information to related order"""

        user_pk = data.data['user']
        user = Users.objects.get(pk=user_pk)
        account = Accounts.objects.get(pk=user.account.id)

        return {
            'account_id': account.id,
            'full_name': user.full_name,
            'phone_number': user.phone_number,
            'user_location': user.user_location,
            'email': account.email,
        }

    def _alter_car_wash_information(self, data: serializer_class) -> dict:
        """Add full car wash information to related order"""

        car_wash_pk = data.data['car_wash']
        car_wash = CarWashes.objects.get(pk=car_wash_pk)

        return {
            'car_wash_id': car_wash.id,
            'car_wash_name': car_wash.car_wash_name,
            'car_wash_address': car_wash.car_wash_address,
            'quantity_of_places': car_wash.quantity_of_places,
        }

    def retrieve(self, request, *args: tuple, **kwargs: dict) -> serializer_class:
        """
        Re-write default retrieve method to alter the returned data
        """

        data = super().retrieve(request, *args, **kwargs)
        data.data['user'] = self._alter_user_information(data)
        data.data['car_wash'] = self._alter_car_wash_information(data)
        return data
