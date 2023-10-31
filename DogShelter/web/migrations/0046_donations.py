# Generated by Django 4.1.3 on 2022-11-14 21:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0045_delete_donations"),
    ]

    operations = [
        migrations.CreateModel(
            name="Donations",
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
                (
                    "amount",
                    models.DecimalField(
                        blank=True, decimal_places=2, default=0.0, max_digits=7
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("EUR", "EUR"),
                            ("BGN", "BGN"),
                            ("GBP", "GBP"),
                            ("USD", "USD"),
                        ],
                        default="BGN",
                        max_length=3,
                    ),
                ),
                (
                    "year_month",
                    models.DateField(
                        blank=True,
                        default=datetime.datetime(
                            2022,
                            11,
                            14,
                            21,
                            33,
                            13,
                            266034,
                            tzinfo=datetime.timezone.utc,
                        ),
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="web.people",
                        verbose_name="Virtual Adopter",
                    ),
                ),
            ],
        ),
    ]
