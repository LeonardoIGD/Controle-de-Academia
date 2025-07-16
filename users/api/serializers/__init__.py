""" This module imports all serializers for the users app. """
# Serializers

from .instructor_serializer import (InstructorProfileReadDetailSerializer,
                                    InstructorProfileReadSerializer,
                                    InstructorProfileWriteSerializer)
from .student_serializer import (StudentProfileReadDetailSerializer,
                                 StudentProfileReadSerializer,
                                 StudentProfileWriteSerializer)
