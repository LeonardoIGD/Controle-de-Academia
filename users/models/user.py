""" Module that provides functions for UUID generation """
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from users.managers import CustomUserManager


class User(AbstractUser):
    """ Base model that will represent all users of the system """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="Identificador"
    )

    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Nome de usuário"
    )

    email = models.EmailField(
        unique=True,
        verbose_name="E-mail"
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Telefone"
    )

    is_student = models.BooleanField(
        default=False,
        verbose_name="É aluno?"
    )

    is_instructor = models.BooleanField(
        default=False,
        verbose_name="É instrutor?"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em"
    )

    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    class Meta:
        """ Class that defines the model metadata """
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.username} ({self.email})"

    def save(self, *args, **kwargs):
        if self.is_instructor and self.is_student:
            raise ValueError("Um usuário não pode ser aluno e instrutor ao mesmo tempo")

        super().save(*args, **kwargs)
