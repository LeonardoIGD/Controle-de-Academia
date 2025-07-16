"""
    This file is part of the gym application, which contains serializers
    for handling API requests related to gym operations.
"""

# Serializers
from .enrollment_serializer import (
    EnrollmentReadSerializer,
    EnrollmentReadDetailSerializer,
    EnrollmentWriteSerializer,
)
from .plan_serializer import (
    PlanReadSerializer,
    PlanReadDetailSerializer,
    PlanWriteSerializer,
)
