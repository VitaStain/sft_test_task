from django.contrib import admin

from apps.contract.models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "created_at",
    )
    readonly_fields = ("created_at", "updated_at")
