from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from core.models import BaseModel
from users.models import InstructorProfile


class Plan(BaseModel):
    name = models.CharField(
        max_length=100,
        verbose_name="Nome do Plano"
    )

    description = models.TextField(
        verbose_name="Descrição"
    )

    duration_months = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Duração (meses)"
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Preço"
    )

    modality = models.CharField(
        max_length=100, 
        verbose_name="Modalidade"
    )

    max_students = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Limite de Alunos"
    )

    instructor = models.ForeignKey(
        InstructorProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="plans",
        verbose_name="Instrutor Responsável"
    )

    class Meta:
        verbose_name = "Plano"
        verbose_name_plural = "Planos"

    def __str__(self):
        return f"{self.name} ({self.duration_months} meses)"

