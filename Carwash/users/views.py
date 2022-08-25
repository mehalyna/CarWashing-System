from rest_framework import viewsets, permissions
from rest_framework.authentication import BasicAuthentication

from users.models import Users
from users.serializers import UsersSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Users API view to list, edit and delete users.
    """

    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [BasicAuthentication]
