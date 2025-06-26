from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from gym.models import Enrollment
from gym.api.serializers import (
    EnrollmentReadSerializer,
    EnrollmentReadDetailSerializer,
    EnrollmentWriteSerializer,
)


@extend_schema(tags=['API Enrollment Management'])
class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.filter(active=True).select_related('student', 'plan', 'assigned_by')
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return EnrollmentReadSerializer
        elif self.action == 'retrieve':
            return EnrollmentReadDetailSerializer
        
        return EnrollmentWriteSerializer

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()
