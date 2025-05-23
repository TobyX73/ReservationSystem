# Generated by Django 5.1.7 on 2025-04-22 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=255)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('website', models.URLField(blank=True, null=True)),
                ('rating', models.FloatField(default=0.0)),
                ('cuisineType', models.CharField(max_length=50)),
            ],
        ),
    ]
