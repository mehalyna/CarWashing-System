from rest_framework import viewsets, permissions

from users.models import Users
from users.serializers import UsersSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticated]
