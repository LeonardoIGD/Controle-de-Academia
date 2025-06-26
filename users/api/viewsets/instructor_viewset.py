from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from users.models import InstructorProfile
from users.api.serializers import (
    InstructorProfileReadSerializer,
    InstructorProfileReadDetailSerializer,
    InstructorProfileWriteSerializer,
)

@extend_schema(tags=['API Instructor Management'])
class InstructorProfileViewSet(viewsets.ModelViewSet):
    queryset = InstructorProfile.objects.filter(active=True)
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return InstructorProfileReadSerializer
        elif self.action == 'retrieve':
            return InstructorProfileReadDetailSerializer
        
        return InstructorProfileWriteSerializer

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()
