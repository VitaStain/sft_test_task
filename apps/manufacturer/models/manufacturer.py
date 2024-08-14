from django.db import models

from core.mixins.models import CreatedUpdatedAtMixin


class Manufacturer(CreatedUpdatedAtMixin, models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
