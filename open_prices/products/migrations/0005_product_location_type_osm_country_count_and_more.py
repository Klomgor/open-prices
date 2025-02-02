# Generated by Django 5.1.4 on 2025-02-02 17:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_product_proof_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="location_type_osm_country_count",
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="price_currency_count",
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
