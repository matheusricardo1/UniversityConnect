# Generated by Django 4.2.2 on 2023-07-01 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "UniversityConnect",
            "0004_curso_mini_descricao_curso_mini_description_en_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="curso",
            name="descricao",
            field=models.TextField(max_length=900),
        ),
        migrations.AlterField(
            model_name="curso",
            name="description_en",
            field=models.TextField(default="English Description", max_length=900),
        ),
    ]
