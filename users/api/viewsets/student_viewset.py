"""
    Imports for Student Profile API viewsets.

    Django REST Framework components:
    - viewsets: Module for ViewSet classes implementation
    - permissions.IsAuthenticated: Permission class for authenticated access
    - drf_spectacular.extend_schema: Decorator for OpenAPI schema customization

    Local application imports:
    - StudentProfile: Model from users app
    - StudentProfile serializers:
    * ReadSerializer: Basic read serializer
    * ReadDetailSerializer: Detailed read serializer 
    * WriteSerializer: Serializer for write operations
"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from users.models import StudentProfile
from users.api.serializers import (
    StudentProfileReadSerializer,
    StudentProfileReadDetailSerializer,
    StudentProfileWriteSerializer,
)


@extend_schema(tags=['API Student Management'])
class StudentProfileViewSet(viewsets.ModelViewSet):
    """
    API ViewSet for managing Student Profiles.

    Provides CRUD operations for StudentProfile model with soft delete functionality.
    Only active profiles are returned by default.
    """
    queryset = StudentProfile.objects.filter(active=True) # pylint: disable=no-member
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return StudentProfileReadSerializer
        elif self.action == 'retrieve':
            return StudentProfileReadDetailSerializer

        return StudentProfileWriteSerializer

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()
