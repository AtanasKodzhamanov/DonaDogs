# Generated by Django 4.1 on 2022-11-06 03:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "web",
            "0019_rename_donation_descriptionbg_donations_donation_description_bg_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="dog",
            old_name="pic2",
            new_name="pic_2",
        ),
        migrations.RenameField(
            model_name="dog",
            old_name="pic3",
            new_name="pic_3",
        ),
        migrations.RenameField(
            model_name="dog",
            old_name="pic4",
            new_name="pic_4",
        ),
        migrations.RenameField(
            model_name="dog",
            old_name="pic5",
            new_name="pic_5",
        ),
        migrations.RenameField(
            model_name="dog",
            old_name="story_BG",
            new_name="story_bg",
        ),
        migrations.RenameField(
            model_name="dog",
            old_name="story_ENG",
            new_name="story_eng",
        ),
    ]
