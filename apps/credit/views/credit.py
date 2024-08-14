from django.contrib.postgres.aggregates import ArrayAgg
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics

from apps.credit.models import Credit
from apps.credit.serializers.credit import CreditSerializer


@extend_schema(tags=["credits"])
@extend_schema_view(
    get=extend_schema(summary="Get credits"),
)
class CreditListView(generics.ListAPIView):
    queryset = Credit.objects.all().annotate(
        unique_manufactures=ArrayAgg("products__manufacturer__id", distinct=True)
    )
    serializer_class = CreditSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = {
        "contract__id": ["exact"],
    }
