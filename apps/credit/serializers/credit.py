from rest_framework import serializers

from apps.credit.models import Credit


class CreditSerializer(serializers.ModelSerializer):
    unique_manufactures = serializers.ListField()

    class Meta:
        model = Credit
        fields = ["id", "unique_manufactures"]
