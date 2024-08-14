from django.contrib import admin

from apps.manufacturer.models import Manufacturer


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "created_at",
    )
    readonly_fields = ("created_at", "updated_at")
