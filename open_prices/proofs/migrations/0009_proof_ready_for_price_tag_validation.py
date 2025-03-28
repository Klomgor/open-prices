# Generated by Django 5.1.4 on 2024-12-26 16:37

from django.db import migrations, models


def init_ready_for_price_tag_validation(apps, schema_editor):
    Proof = apps.get_model("proofs", "Proof")
    Proof.objects.filter(type="PRICE_TAG", source__contains="/proofs/add/").update(
        ready_for_price_tag_validation=True
    )


class Migration(migrations.Migration):
    dependencies = [
        ("proofs", "0008_alter_proofprediction_type_pricetagprediction"),
    ]

    operations = [
        migrations.AddField(
            model_name="proof",
            name="ready_for_price_tag_validation",
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(init_ready_for_price_tag_validation),
    ]
