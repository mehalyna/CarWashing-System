from django.contrib import admin

from CW_places.models import CWPlaces


@admin.register(CWPlaces)
class OrderAdmin(admin.ModelAdmin):
    """
        Create methods to handle actions
        Create a list - 'actions' and store the names of all custom methods
        Fields to be shown in admin panel with list_display
        Fields to be editable in admin panel with list_editable
    """

    def make_carwash_available(self, request, queryset):
        queryset.update(is_free=True)

    make_carwash_available.short_description = "Mark selected carwash as available"

    def make_carwash_unavailable(self, request, queryset):
        queryset.update(is_free=False)

    make_carwash_unavailable.short_description = "Mark selected carwash as unavailable"

    actions = [make_carwash_available, make_carwash_unavailable]
    list_display = ('carwash_place', "added", 'place', "is_free")
    list_editable = ['place']

