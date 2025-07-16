"""
    This file is part of the gym application, which contains serializers
    for handling API requests related to gym operations.
"""

# Serializers
from .enrollment_serializer import (EnrollmentReadDetailSerializer,
                                    EnrollmentReadSerializer,
                                    EnrollmentWriteSerializer)
from .plan_serializer import (PlanReadDetailSerializer, PlanReadSerializer,
                              PlanWriteSerializer)
