from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from users.models import Users

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_user(instance, created, **kwargs):
    """
    Creates user right after an account is created.
    """
    if created:
        Users.objects.create(
            account=instance
        )


@receiver(post_delete, sender=Users)
def delete_account(instance, **kwargs):
    """
    Deletes the account that is connected to the User instance.
    """
    instance.account.delete()
