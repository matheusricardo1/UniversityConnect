# Generated by Django 4.2.2 on 2023-09-21 12:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("UniversityConnect", "0022_alter_exstudent_biography_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exstudent",
            name="birth_date",
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1000),
                    django.core.validators.MaxValueValidator(9999),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="exstudent",
            name="death_date",
            field=models.PositiveIntegerField(
                blank=True,
                default=None,
                validators=[
                    django.core.validators.MinValueValidator(1000),
                    django.core.validators.MaxValueValidator(9999),
                ],
            ),
        ),
    ]
