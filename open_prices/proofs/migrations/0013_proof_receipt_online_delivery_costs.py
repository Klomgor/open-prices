# Generated by Django 5.1.4 on 2025-02-23 14:06

from decimal import Decimal

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("proofs", "0012_alter_pricetag_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="proof",
            name="receipt_online_delivery_costs",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                validators=[django.core.validators.MinValueValidator(Decimal("0"))],
                verbose_name="Receipt's online delivery costs (user input)",
            ),
        ),
    ]
