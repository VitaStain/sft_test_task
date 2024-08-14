from rest_framework import serializers

from apps.credit.models import Credit
from apps.manufacturer.models import Manufacturer


class CreditSerializer(serializers.ModelSerializer):
    unique_manufactures = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Credit
        fields = ["id", "unique_manufactures"]

    def get_unique_manufactures(self, obj: Credit) -> list[int]:
        return (
            Manufacturer.objects.filter(products__credit=obj)
            .distinct()
            .values_list("id", flat=True)
        )
