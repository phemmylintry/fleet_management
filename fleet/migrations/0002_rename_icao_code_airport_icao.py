# Generated by Django 4.0.1 on 2022-01-24 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airport',
            old_name='icao_code',
            new_name='icao',
        ),
    ]
