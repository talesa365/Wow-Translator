# Generated by Django 4.1.4 on 2022-12-28 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Input",
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
                ("content", models.CharField(max_length=9999, unique=True)),
                ("character_length", models.CharField(max_length=4)),
            ],
        ),
    ]
