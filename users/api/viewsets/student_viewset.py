from rest_framework import viewsets, status
from rest_framework.response import Response
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
    queryset = StudentProfile.objects.filter(active=True)
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
