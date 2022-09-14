"""
Django file for configuration of order_details application.
"""

from django.apps import AppConfig


class OrderDetailsConfig(AppConfig):
    """
    Class for order_details application configurations.
    Drop-in replacement for str(obj) that tries to be Unicode friendly.

    default_auto_field sets 64-bit integer for primary key in models.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order_details'
