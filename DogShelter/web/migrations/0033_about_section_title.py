# Generated by Django 4.1.3 on 2022-11-12 00:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0032_about_noticeboard_location_alter_dog_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="about",
            name="section_title",
            field=models.TextField(blank=True, default="", max_length=100),
        ),
    ]
