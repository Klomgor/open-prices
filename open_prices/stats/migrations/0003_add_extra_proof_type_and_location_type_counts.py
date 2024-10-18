# Generated by Django 5.1 on 2024-10-18 08:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stats", "0002_add_proof_type_counts"),
    ]

    operations = [
        migrations.AddField(
            model_name="totalstats",
            name="location_type_online_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="totalstats",
            name="location_type_osm_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="totalstats",
            name="proof_type_gdpr_request_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="totalstats",
            name="proof_type_shop_import_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
