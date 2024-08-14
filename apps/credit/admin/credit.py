from django.contrib import admin

from apps.credit.models import Credit


@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "created_at",
    )
    readonly_fields = ("created_at", "updated_at")
    raw_id_fields = ("contract",)
