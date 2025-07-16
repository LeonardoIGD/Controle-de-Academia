"""
    Imports for Instructor Profile API viewsets.

    Django REST Framework components:
    - viewsets: Module for ViewSet classes implementation
    - permissions.IsAuthenticated: Permission class for authenticated access
    - drf_spectacular.extend_schema: Decorator for OpenAPI schema customization

    Local application imports:
    - Plan: Model from gym app
    - Plan serializers:
    * PlanReadSerializer: Basic read serializer
    * PlanReadDetailSerializer: Detailed read serializer
    * PlanWriteSerializer: Serializer for write operations
"""

from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from gym.api.serializers import (PlanReadDetailSerializer, PlanReadSerializer,
                                 PlanWriteSerializer)
from gym.models import Plan


@extend_schema(tags=['API Plan Management'])
class PlanViewSet(viewsets.ModelViewSet):
    """
    API ViewSet for managing Plans.

    Provides CRUD operations for Plans model with soft delete functionality.
    Only active plans are returned by default.
    """

    queryset = Plan.objects.filter(active=True)  # pylint: disable=no-member
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return PlanReadSerializer

        if self.action == 'retrieve':
            return PlanReadDetailSerializer

        return PlanWriteSerializer

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()
