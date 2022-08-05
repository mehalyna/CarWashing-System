from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from users.managers import AccountsManager


class Accounts(AbstractBaseUser, PermissionsMixin):
    """
    Users will authenticate with email and password.
    """
    email = models.EmailField(
        unique=True,
        null=False
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'

    objects = AccountsManager()


class Users(models.Model):
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        null=True
    )

    full_name = models.CharField(
        max_length=100,
        null=True
    )
    user_location = models.CharField(
        max_length=100,
        null=True
    )

    account = models.OneToOneField(
        Accounts,
        on_delete=models.CASCADE,
        primary_key=True,
    )
