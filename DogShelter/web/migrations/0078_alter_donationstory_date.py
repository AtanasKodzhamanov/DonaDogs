# Generated by Django 4.1.2 on 2022-12-24 05:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0077_alter_donationstory_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="donationstory",
            name="date",
            field=models.DateField(
                blank=True,
                default=datetime.date(2022, 11, 30),
                help_text="Дата на дарението. По подразбиране е последният ден на предходния месец. Например ако дарението е направено на 1.01.2020, то по подразбиране ще се показва на 31.12.2019. Това е за да се показват даренията в последния месец.",
            ),
        ),
    ]
