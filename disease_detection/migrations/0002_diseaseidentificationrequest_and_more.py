# Generated by Django 5.0.7 on 2024-07-15 12:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("disease_detection", "0001_initial"),
        ("plant_disease", "0002_diseasecategory_plant_plantpart_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DiseaseIdentificationRequest",
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
                ("request_time", models.DateTimeField(auto_now_add=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="disease_identification/"
                    ),
                ),
                ("ai_requested", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="diagnosticsession",
            name="plant",
        ),
        migrations.RemoveField(
            model_name="diagnosticsession",
            name="user",
        ),
        migrations.DeleteModel(
            name="DiseaseCategory",
        ),
        migrations.DeleteModel(
            name="PlantPart",
        ),
        migrations.DeleteModel(
            name="DiagnosticSession",
        ),
    ]
