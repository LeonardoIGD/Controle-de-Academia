import uuid

from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
        verbose_name="Identificador"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de criação",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Data de atualização",
    )

    created_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        blank=True,
        verbose_name="Criando por",
    )

    class Meta:
        abstract = True
