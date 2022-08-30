from django.contrib import admin

from users.models import Users, Accounts


@admin.register(Accounts)
class AccountsAdmin(admin.ModelAdmin):
    """
    At Accounts admin panel:
        - accounts can be searched by their email.
        - accounts emails and statuses are listed.
        - accounts can be filtered by their status.
    """

    search_fields = ('email__contains', )
    list_display = ('email', 'is_superuser', 'is_staff', 'is_active')
    list_filter = ('is_superuser', 'is_staff')


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    """
    At Users admin panel:
        - users can be searched by their full name and phone number.
        - users full names, phone numbers and connected accounts are listed.
        - users can be filtered by their location.
    """

    search_fields = ('full_name__contains', 'phone_number__contains')
    list_display = ('full_name', 'phone_number', 'account')
    list_filter = ('user_location', )
