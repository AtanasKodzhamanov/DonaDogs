# Generated by Django 4.1.3 on 2022-11-12 01:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0035_remove_about_note_pic_2_about_note_p"),
    ]

    operations = [
        migrations.RenameField(
            model_name="about",
            old_name="note_p",
            new_name="about_pic_2",
        ),
    ]
