# Generated by Django 5.1 on 2024-09-27 15:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("locations", "0003_location_product_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="location",
            name="user_count",
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
