# Generated by Django 5.0.7 on 2024-08-07 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scientists', '0003_image_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('source', models.CharField(max_length=255)),
                ('record_count', models.IntegerField()),
                ('creation_date', models.DateField()),
                ('license', models.CharField(blank=True, max_length=100, null=True)),
                ('data_fields', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiseaseReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_id', models.CharField(max_length=100)),
                ('plant_type', models.CharField(max_length=100)),
                ('symptoms', models.TextField()),
                ('diagnosis', models.TextField()),
                ('treatment', models.TextField()),
                ('date_of_incident', models.DateField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('submitted_by', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True, null=True)),
                ('severity', models.CharField(blank=True, choices=[('Low', 'Low'), ('Moderate', 'Moderate'), ('High', 'High'), ('Severe', 'Severe')], max_length=20, null=True)),
                ('environmental_conditions', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SciencePaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('abstract', models.TextField()),
                ('authors', models.TextField()),
                ('publication_date', models.DateField()),
                ('doi', models.CharField(blank=True, max_length=100, null=True)),
                ('keywords', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
