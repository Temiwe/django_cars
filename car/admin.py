from django.contrib import admin
from .models import Car, CarModel, Company, CarColor, CarDate, CarType


# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        'vin_number',
        'car_model',
        "car_color",
        "car_date",
        "car_type",
        "company"
    ]
    fieldsets = (
        (None, {
            'fields': (
                ("name", "vin_number")
            )
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ("car_model", "car_color", "car_date", "car_type"),
        }),
    )
    readonly_fields = [
        "company"
    ]


class CarInline(admin.StackedInline):
    model = Car


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]

    inlines = [
        CarInline
    ]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]


@admin.register(CarColor)
class CarColorAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]


@admin.register(CarDate)
class CarDateAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]

@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]

