# Generated by Django 4.2.2 on 2023-09-20 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("UniversityConnect", "0020_rename_tittle_en_course_title_en"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="course",
            name="description_en",
            field=models.TextField(default="English Description"),
        ),
    ]
