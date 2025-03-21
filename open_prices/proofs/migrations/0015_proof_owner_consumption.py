# Generated by Django 5.1.4 on 2025-03-06 23:23

from django.db import migrations, models

from open_prices.proofs import constants as proof_constants


def init_owner_consumption(apps, schema_editor):
    Proof = apps.get_model("proofs", "Proof")
    Proof.objects.filter(type__in=proof_constants.TYPE_GROUP_CONSUMPTION_LIST).update(
        owner_consumption=True
    )


class Migration(migrations.Migration):
    dependencies = [
        ("proofs", "0014_proof_owner_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="proof",
            name="owner_consumption",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.RunPython(init_owner_consumption),
    ]
