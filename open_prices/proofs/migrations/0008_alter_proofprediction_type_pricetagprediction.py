# Generated by Django 5.1.4 on 2024-12-17 14:01

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("proofs", "0007_pricetag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="proofprediction",
            name="type",
            field=models.CharField(
                choices=[
                    ("OBJECT_DETECTION", "OBJECT_DETECTION"),
                    ("CLASSIFICATION", "CLASSIFICATION"),
                    ("RECEIPT_EXTRACTION", "RECEIPT_EXTRACTION"),
                ],
                max_length=20,
                verbose_name="The type of the prediction",
            ),
        ),
        migrations.CreateModel(
            name="PriceTagPrediction",
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
                    "type",
                    models.CharField(
                        choices=[("PRICE_TAG_EXTRACTION", "PRICE_TAG_EXTRACTION")],
                        help_text="The type of the prediction",
                        max_length=20,
                    ),
                ),
                (
                    "model_name",
                    models.CharField(
                        help_text="The name of the model that generated the prediction",
                        max_length=30,
                    ),
                ),
                (
                    "model_version",
                    models.CharField(
                        help_text="The specific version of the model that generated the prediction",
                        max_length=30,
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="When the prediction was created in DB",
                    ),
                ),
                (
                    "data",
                    models.JSONField(
                        default=dict,
                        help_text="a dict representing the data of the prediction. This field is model-specific.",
                    ),
                ),
                (
                    "price_tag",
                    models.ForeignKey(
                        help_text="The price tag this prediction belongs to",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="predictions",
                        to="proofs.pricetag",
                    ),
                ),
            ],
            options={
                "verbose_name": "Price Tag Prediction",
                "verbose_name_plural": "Price Tag Predictions",
                "db_table": "price_tag_predictions",
            },
        ),
    ]
