# Generated by Django 5.2.3 on 2025-06-26 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructorprofile',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Ativo?'),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Ativo?'),
        ),
    ]
