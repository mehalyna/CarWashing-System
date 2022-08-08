from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from users.models import Users
from users.serializers import UsersSerializer


class UsersList(ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UserDetails(RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    lookup_url_kwarg = 'pk'
