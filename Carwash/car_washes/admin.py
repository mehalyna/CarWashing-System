from django.contrib import admin

from car_washes.models import CarWashes
from car_washes.tasks import car_wash_task

# Connect custom action and celery task

class CarWashAdmin(admin.ModelAdmin):
    model = CarWashes
    list_display = ('id', 'car_wash_name', 'car_wash_address', 'quantity_of_places')
    list_display_links = ('id', 'car_wash_name')
    search_fields = ('car_wash_name',)
    list_per_page = 25
    actions = ('car_wash_task',)

    # def make_quantity_0(self, request, queryset):
    #     queryset.update(quantity_of_places=0)


admin.site.register(CarWashes, CarWashAdmin)
