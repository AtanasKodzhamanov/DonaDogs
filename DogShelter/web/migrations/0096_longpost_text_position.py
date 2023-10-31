# Generated by Django 4.1.6 on 2023-02-21 06:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0095_longpost_text_align"),
    ]

    operations = [
        migrations.AddField(
            model_name="longpost",
            name="text_position",
            field=models.CharField(
                choices=[("top", "Top"), ("bottom", "Botton")],
                default="top",
                help_text="Изберете позицията на текста в контейнера. Горе или долу.",
                max_length=6,
            ),
        ),
    ]
