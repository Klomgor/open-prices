# Generated by Django 5.1 on 2024-09-27 15:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("locations", "0002_location_proof_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="location",
            name="product_count",
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
