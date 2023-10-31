# Generated by Django 4.1 on 2022-09-18 01:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0002_donations_alter_dog_virtual_adopter"),
    ]

    operations = [
        migrations.CreateModel(
            name="Adoptions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("adoption_descriptionENG", models.TextField(blank=True, default="")),
                ("adoption_descriptionBG", models.TextField(blank=True, default="")),
                ("adoption_pic_before", models.URLField(max_length=300, null=True)),
                ("adoption_pic_after1", models.URLField(max_length=300)),
                ("adoption_pic_after2", models.URLField(max_length=300)),
                ("adoption_video", models.URLField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="NoticeBoard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("noticeENG", models.TextField(blank=True, default="")),
                ("noticeBG", models.TextField(blank=True, default="")),
                ("notice_pic1", models.URLField(max_length=300)),
                ("notice_pic2", models.URLField(max_length=300)),
            ],
        ),
    ]
