""" This module imports all serializers for the users app. """
# Serializers

from .instructor_serializer import (
    InstructorProfileReadSerializer,
    InstructorProfileReadDetailSerializer,
    InstructorProfileWriteSerializer,
)
from .student_serializer import (
    StudentProfileReadSerializer,
    StudentProfileReadDetailSerializer,
    StudentProfileWriteSerializer,
)
