from django.core.management.base import BaseCommand
from django.db import transaction

from apps.contract.models import Contract
from apps.credit.models import Credit
from apps.manufacturer.models import Manufacturer
from apps.product.models import Product


class Command(BaseCommand):
    help = "Delete database without pictures"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        Contract.objects.all().delete()
        Manufacturer.objects.all().delete()
        Product.objects.all().delete()
        Credit.objects.all().delete()
