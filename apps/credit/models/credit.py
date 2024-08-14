from django.db import models

from apps.contract.models.contract import Contract
from core.mixins.models import CreatedUpdatedAtMixin


class Credit(CreatedUpdatedAtMixin, models.Model):
    name = models.CharField(max_length=255)
    contract = models.OneToOneField(
        Contract, on_delete=models.CASCADE, related_name="credit"
    )

    def __str__(self):
        return self.name
