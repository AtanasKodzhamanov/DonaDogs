# Generated by Django 4.1 on 2022-11-06 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_alter_dog_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name_eng', models.CharField(max_length=60, null=True, unique=True)),
                ('person_name_bg', models.CharField(default='', max_length=60)),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
        migrations.AlterField(
            model_name='adoptions',
            name='DogNameENG',
            field=models.CharField(max_length=60, null=True, unique=True),
        ),
    ]
