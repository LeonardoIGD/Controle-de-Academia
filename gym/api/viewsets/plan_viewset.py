from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from gym.models import Plan
from gym.api.serializers import (
    PlanReadSerializer,
    PlanReadDetailSerializer,
    PlanWriteSerializer,
)


@extend_schema(tags=['API Plan Management'])
class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.filter(active=True)
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return PlanReadSerializer
        elif self.action == 'retrieve':
            return PlanReadDetailSerializer
        
        return PlanWriteSerializer

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()
