from rest_framework import serializers
from .models import NormalizationUnit


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalizationUnit
        fields = ("unit_name", "count_unit", "price_unit", "price", "fromurl", "update_time")
