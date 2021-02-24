from .models import NormalizationUnit
from .serializers import UnitSerializer
from rest_framework import generics


class UnitListCreate(generics.ListCreateAPIView):
    queryset = NormalizationUnit.objects.all()
    serializer_class = UnitSerializer