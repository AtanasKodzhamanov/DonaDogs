# Generated by Django 4.1 on 2022-11-08 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0030_alter_dog_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptions',
            name='adoption_year',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
