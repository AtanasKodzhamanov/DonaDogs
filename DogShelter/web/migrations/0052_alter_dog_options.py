# Generated by Django 4.1.3 on 2022-11-19 08:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0051_alter_about_section_desc_eng"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dog",
            options={"ordering": ("-pk",)},
        ),
    ]
