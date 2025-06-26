from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from core.models import BaseModel
from .user import User

class StudentProfile(BaseModel):
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
        verbose_name = "Perfil de Aluno"
        verbose_name_plural = "Perfis de Alunos"
    
    def __str__(self):
        return f"Perfil de {self.user.username}"
    
    @property
    def bmi(self):
        if self.height and self.weight:
            return round(self.weight / (self.height ** 2), 2)
        
        return None
