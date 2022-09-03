from django.contrib import admin

from car_washes.models import CarWashes
from car_washes.tasks import set_car_wash_quantity_to_0


class CarWashAdmin(admin.ModelAdmin):
    model = CarWashes
    list_display = ('id', 'car_wash_name', 'car_wash_address', 'quantity_of_places')
    list_display_links = ('id', 'car_wash_name')
    search_fields = ('car_wash_name',)
    list_per_page = 25
    actions = ('make_quantity_0',)

    def make_quantity_0(self, request, queryset):
        for car_wash in queryset:
            set_car_wash_quantity_to_0.delay(car_wash.id)


admin.site.register(CarWashes, CarWashAdmin)
