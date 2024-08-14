from random import choice

from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker

from apps.contract.models import Contract
from apps.credit.models import Credit
from apps.manufacturer.models import Manufacturer
from apps.product.models import Product


class Command(BaseCommand):
    help = "Fill database by data"

    @staticmethod
    def create_credit(fakes):
        for _ in range(20):
            contract = Contract.objects.create(
                name=fakes.word(),
            )
            Credit.objects.create(
                name=fakes.word(),
                contract=contract,
            )

    @staticmethod
    def create_manufacturer(fakes):
        for _ in range(20):
            manufacturer = Manufacturer.objects.create(
                name=fakes.word(),
            )

    @staticmethod
    def create_product(fakes):
        manufacturers = Manufacturer.objects.all()
        credit = Credit.objects.all()

        for _ in range(20):
            product = Product.objects.create(
                name=fakes.word(),
                manufacturer=choice(manufacturers),
                credit=choice(credit),
            )

    @transaction.atomic
    def handle(self, *args, **kwargs):
        fakes = Faker("en_US")
        self.create_credit(fakes)
        self.create_manufacturer(fakes)
        self.create_product(fakes)
