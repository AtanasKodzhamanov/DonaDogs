# Generated by Django 4.1.3 on 2022-11-15 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0048_people_virtual_adopter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='monthly_upkeep',
        ),
    ]
