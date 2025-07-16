""" Module that provides functions for UUID generation """
import uuid

from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    """ Base system model """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="Identificador"
    )

    active = models.BooleanField(
        default=True,
        verbose_name="Ativo?"
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
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Criando por",
    )

    class Meta:
        """ Class that defines the model metadata """
        abstract = True
