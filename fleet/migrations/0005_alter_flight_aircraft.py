# Generated by Django 4.0.1 on 2022-01-25 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0004_airport_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='aircraft',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aircraft_flights', to='fleet.aircraft'),
        ),
    ]
