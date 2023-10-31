# Generated by Django 4.1.2 on 2022-12-25 04:10

import DogShelter.web.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0081_alter_donationstory_date_pk"),
    ]

    operations = [
        migrations.AddField(
            model_name="donationstory",
            name="title_bg",
            field=models.CharField(
                default="",
                help_text="Заглавие на дарението на Български.",
                max_length=100,
                validators=[DogShelter.web.validators.validate_bulgarian],
            ),
        ),
        migrations.AddField(
            model_name="donationstory",
            name="title_eng",
            field=models.CharField(
                default="",
                help_text="Заглавие на дарението на Английски.",
                max_length=100,
                validators=[DogShelter.web.validators.validate_english],
            ),
        ),
    ]
