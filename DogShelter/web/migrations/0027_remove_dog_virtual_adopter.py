# Generated by Django 4.1 on 2022-11-06 03:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0026_dog_person"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dog",
            name="virtual_adopter",
        ),
    ]
