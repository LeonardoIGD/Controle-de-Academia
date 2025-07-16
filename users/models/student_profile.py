"""
    Module containing necessary imports for Django model definitions.

    Django imports:
    - models: Main module for database model definitions
    - ValidationError: Exception for model field validation
    - validators: Field validators (MinValueValidator and MaxValueValidator)

    Local imports:
    - BaseModel: Abstract base model with common fields (from core app)
    - User: Custom user model (from current module)
"""

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.models import BaseModel

from .user import User


class StudentProfile(BaseModel):
    """ Model representing the system's student profiles """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='student_profile',
        verbose_name="Usuário",
        limit_choices_to={'is_student': True}
    )

    birth_date = models.DateField(
        verbose_name="Data de Nascimento"
    )

    height = models.FloatField(
        validators=[MinValueValidator(0.5), MaxValueValidator(2.5)],
        verbose_name="Altura (metros)"
    )

    weight = models.FloatField(
        validators=[MinValueValidator(30), MaxValueValidator(300)],
        verbose_name="Peso (kg)"
    )

    health_restrictions = models.TextField(
        blank=True,
        verbose_name="Restrições de Saúde"
    )

    fitness_goals = models.TextField(
        blank=True,
        verbose_name="Objetivos Fitness"
    )

    class Meta:
        """ Class that defines the model metadata """
        verbose_name = "Perfil de Aluno"
        verbose_name_plural = "Perfis de Alunos"

    def __str__(self):
        return f"Perfil de {self.user.username}" # pylint: disable=no-member

    def clean(self):
        if not self.user.is_student: # pylint: disable=no-member
            raise ValidationError("Usuário não está marcado como aluno.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    @property
    def bmi(self):
        """ Property that calculates the BMI based on the student's height and weight """
        if self.height and self.weight:
            return round(self.weight / (self.height ** 2), 2)

        return None
