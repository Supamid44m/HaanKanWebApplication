# Generated by Django 4.0 on 2023-01-31 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Party', '0057_party_evidence_of_payment_party_uploaded_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='party',
            old_name='evidence_of_payment',
            new_name='evidenceimage',
        ),
    ]
