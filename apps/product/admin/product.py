from django.contrib import admin

from apps.product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "created_at",
    )
    readonly_fields = ("created_at", "updated_at")
    raw_id_fields = ("credit", "manufacturer")
