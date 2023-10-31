# Generated by Django 4.1.2 on 2022-12-24 05:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0075_donationstory_donation_pic_5_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="donationstory",
            name="date",
            field=models.DateField(
                help_text="Дата на дарението. По подразбиране е последният ден на предходния месец. Например ако дарението е направено на 1.01.2020, то по подразбиране ще се показва на 31.12.2019. Това е за да се показват даренията в последния месец.",
                max_length=7,
            ),
        ),
    ]
