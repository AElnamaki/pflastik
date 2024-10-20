# Generated by Django 5.0.7 on 2024-07-16 07:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Foo",
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
                (
                    "user",
                    models.CharField(
                        choices=[("S", "Scientist"), ("F", "Farmer")], max_length=1
                    ),
                ),
            ],
        ),
    ]
