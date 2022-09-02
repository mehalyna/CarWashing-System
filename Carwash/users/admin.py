from django.contrib import admin, messages

from users.models import Users, Accounts


def show_message(model, request, message):
    return model.message_user(request, message, messages.SUCCESS)


@admin.action(description='Make selected accounts superusers')
def make_superuser(model, request, queryset):
    queryset.update(is_superuser=True)
    show_message(model, request, 'Superuser status was successfully changed.')


@admin.action(description='Make selected accounts staff')
def make_staff(model, request, queryset):
    queryset.update(is_staff=True)
    show_message(model, request, 'Staff status was successfully changed.')


@admin.action(description='Make selected accounts regular')
def make_regular(model, request, queryset):
    queryset.update(
        is_superuser=False,
        is_staff=False
    )
    show_message(model, request, 'Superuser and staff statuses were successfully changed.')


@admin.register(Accounts)
class AccountsAdmin(admin.ModelAdmin):
    """
    At Accounts admin panel:
        - accounts can be searched by their email.
        - accounts emails and statuses are listed.
        - accounts can be filtered by their status.
        - selected accounts statuses can be changed via custom actions.
    """

    search_fields = ('email__contains', )
    list_display = ('email', 'is_superuser', 'is_staff', 'is_active')
    list_filter = ('is_superuser', 'is_staff')
    actions = [make_superuser, make_staff, make_regular]


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
