"""
    Enrollment model dependencies and imports.

    Database and Models:
    - django.db.models: Core Django model functionality
    - core.models.BaseModel: Abstract base model with common fields
    - users.models: 
    - StudentProfile: Student information model
    - InstructorProfile: Instructor information model

    Application Specific:
    - .plan.Plan: Subscription plan model
    - .choices.EnrollmentStatus: Status choices for enrollments

    Utilities:
    - dateutil.relativedelta.relativedelta: For advanced date calculations
    and manipulations (e.g., adding months to dates)
"""

from django.db import models

from dateutil.relativedelta import relativedelta

from core.models import BaseModel
from users.models import StudentProfile, InstructorProfile
from .plan import Plan
from .choices import EnrollmentStatus


class Enrollment(BaseModel):
    """ Represents a student's enrollment in a program or course. """
    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name="enrollments",
        verbose_name="Aluno"
    )

    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE,
        related_name="enrollments",
        verbose_name="Plano"
    )

    start_date = models.DateField(
        verbose_name="Data de Início"
    )

    end_date = models.DateField(
        verbose_name="Data de Término",
        blank=True
    )

    status = models.CharField(
        max_length=10,
        choices=EnrollmentStatus.choices,
        default=EnrollmentStatus.ACTIVE,
        verbose_name="Status"
    )

    notes = models.TextField(
        blank=True,
        verbose_name="Observações"
    )

    assigned_by = models.ForeignKey(
        InstructorProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_enrollments",
        verbose_name="Instrutor Responsável"
    )

    class Meta:
        """ Class that defines the model metadata """
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"
        constraints = [
            models.UniqueConstraint(
                fields=["student", "plan"],
                condition=models.Q(active=True),
                name="unique_active_enrollment_per_student_plan"
            )
        ]

    def __str__(self):
        return f"{self.student.user.username} - {self.plan.name}" # pylint: disable=no-member

    def clean(self):
        if self.start_date and self.plan and not self.end_date:
            self.end_date = self.start_date + relativedelta(months=self.plan.duration_months) # pylint: disable=no-member

    def save(self, *args, **kwargs):
        self.full_clean()
        if not self.end_date:
            self.end_date = self.start_date + relativedelta(months=self.plan.duration_months) # pylint: disable=no-member

        super().save(*args, **kwargs)
