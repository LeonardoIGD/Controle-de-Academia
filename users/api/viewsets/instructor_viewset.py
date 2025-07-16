"""
    Imports for Instructor Profile API viewsets.

    Django REST Framework components:
    - viewsets: Module for ViewSet classes implementation
    - permissions.IsAuthenticated: Permission class for authenticated access
    - drf_spectacular.extend_schema: Decorator for OpenAPI schema customization

    Local application imports:
    - InstructorProfile: Model from users app
    - InstructorProfile serializers:
    * ReadSerializer: Basic read serializer
    * ReadDetailSerializer: Detailed read serializer
    * WriteSerializer: Serializer for write operations
"""

from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users.api.serializers import (InstructorProfileReadDetailSerializer,
                                   InstructorProfileReadSerializer,
                                   InstructorProfileWriteSerializer)
from users.models import InstructorProfile


@extend_schema(tags=['API Instructor Management'])
class InstructorProfileViewSet(viewsets.ModelViewSet):
    """
    API ViewSet for managing Instructor Profiles.

    Provides CRUD operations for InstructorProfile model with soft delete functionality.
    Only active profiles are returned by default.
    """

    queryset = InstructorProfile.objects.filter(active=True) # pylint: disable=no-member
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return InstructorProfileReadSerializer

        if self.action == 'retrieve':
            return InstructorProfileReadDetailSerializer

        return InstructorProfileWriteSerializer

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()
