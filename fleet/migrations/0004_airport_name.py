# Generated by Django 4.0.1 on 2022-01-25 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0003_alter_flight_arrival_airport_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=512, null=True),
        ),
    ]
