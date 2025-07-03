"""
    Module containing necessary imports for Django model definitions.

    Django imports:
    - models: Main module for database model definitions
    - ValidationError: Exception for model field validation

    Local imports:
    - BaseModel: Abstract base model with common fields (from core app)
    - User: Custom user model (from current module)
"""

from django.db import models
from django.core.exceptions import ValidationError

from core.models import BaseModel
from .user import User


class InstructorProfile(BaseModel):
    """ Model representing the system's instructor profiles """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='instructor_profile',
        verbose_name="Usuário",
        limit_choices_to={'is_instructor': True}
    )

    specialization = models.CharField(
        max_length=100,
        verbose_name="Especialização"
    )

    certifications = models.TextField(
        verbose_name="Certificações"
    )

    experience_years = models.PositiveIntegerField(
        default=0,
        verbose_name="Anos de Experiência"
    )

    biography = models.TextField(
        blank=True,
        verbose_name="Biografia"
    )

    is_available = models.BooleanField(
        default=True,
        verbose_name="Disponível para novos alunos?"
    )

    class Meta:
        """ Class that defines the model metadata """
        verbose_name = "Perfil de Instrutor"
        verbose_name_plural = "Perfis de Instrutores"

    def __str__(self):
        return f"Instrutor {self.user.username if self.user else 'N/A'}" # pylint: disable=no-member

    def clean(self):
        if not self.user.is_instructor: # pylint: disable=no-member
            raise ValidationError("Usuário não está marcado como instrutor.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
