# Generated by Django 5.1.3 on 2024-11-14 06:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LoggerModel",
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
                ("original_url", models.CharField(max_length=255)),
                ("fake_url", models.CharField(max_length=255)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_app.usermodel",
                    ),
                ),
            ],
        ),
    ]
