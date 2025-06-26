from django.db import models

class EnrollmentStatus(models.TextChoices):
    ACTIVE = 'active', 'Ativa'
    CANCELED = 'canceled', 'Cancelada'
    EXPIRED = 'expired', 'Expirada'
