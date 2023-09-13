# Generated by Django 4.2.2 on 2023-09-13 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("UniversityConnect", "0015_exstudent_image_alter_course_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="New",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                (
                    "image",
                    models.ImageField(blank=True, upload_to="New/cover/%Y/%m/%d/"),
                ),
                ("mini_decription", models.CharField(max_length=255)),
                ("mini_decription_en", models.CharField(default="en", max_length=255)),
                ("text", models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name="exstudent",
            name="image",
            field=models.ImageField(blank=True, upload_to="ExStudents/cover/%Y/%m/%d/"),
        ),
    ]
