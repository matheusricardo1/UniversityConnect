# Generated by Django 4.2.2 on 2023-09-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("UniversityConnect", "0016_new_alter_exstudent_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="new",
            name="mini_decription",
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name="new",
            name="mini_decription_en",
            field=models.CharField(default="en", max_length=300),
        ),
        migrations.AlterField(
            model_name="new",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]
