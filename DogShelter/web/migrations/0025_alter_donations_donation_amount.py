# Generated by Django 4.1 on 2022-11-06 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0024_donations_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='donation_amount',
            field=models.FloatField(default=0),
        ),
    ]
