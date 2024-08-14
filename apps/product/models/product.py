from django.db import models

from apps.credit.models import Credit
from apps.manufacturer.models.manufacturer import Manufacturer
from core.mixins.models import CreatedUpdatedAtMixin


class Product(CreatedUpdatedAtMixin, models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="products"
    )
    credit = models.ForeignKey(
        Credit, on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self):
        return self.name
