# Generated by Django 5.0.7 on 2024-08-10 23:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scientists', '0004_dataset_diseasereport_sciencepaper'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField()),
                ('topics', models.TextField()),
                ('relevance', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='scientists.searchquery')),
            ],
        ),
    ]
