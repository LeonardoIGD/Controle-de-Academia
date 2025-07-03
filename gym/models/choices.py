"""
    Module containing necessary imports for Django model definitions.

    Django imports:
    - models: Main module for database model definitions
"""

from django.db import models

class EnrollmentStatus(models.TextChoices):
    """ Defines possible enrollment status options as text choices. """
    ACTIVE = 'active', 'Ativa'
    CANCELED = 'canceled', 'Cancelada'
    EXPIRED = 'expired', 'Expirada'
