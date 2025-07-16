"""
    Imports for Enrollment API viewsets.

    Django REST Framework components:
    - viewsets: Module for ViewSet classes implementation
    - permissions.IsAuthenticated: Permission class for authenticated access
    - drf_spectacular.extend_schema: Decorator for OpenAPI schema customization

    Local application imports:
    - Enrollment: Model from gym app
    - Enrollment serializers:
    * ReadSerializer: Basic read serializer
    * ReadDetailSerializer: Detailed read serializer
    * WriteSerializer: Serializer for write operations
"""

from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from gym.api.serializers import (EnrollmentReadDetailSerializer,
                                 EnrollmentReadSerializer,
                                 EnrollmentWriteSerializer)
from gym.models import Enrollment


@extend_schema(tags=['API Enrollment Management'])
class EnrollmentViewSet(viewsets.ModelViewSet):
    """
    API ViewSet for managing Instructor Enrollments.

    Provides CRUD operations for Enrollment model with soft delete functionality.
    Only active enrollments are returned by default.
    """

    # pylint: disable=no-member
    queryset = Enrollment.objects.filter(active=True).select_related(
        'student', 'plan', 'assigned_by'
    )
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return EnrollmentReadSerializer

        if self.action == 'retrieve':
            return EnrollmentReadDetailSerializer

        return EnrollmentWriteSerializer

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()
