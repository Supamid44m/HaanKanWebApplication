# Generated by Django 4.0 on 2023-01-31 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Party', '0061_remove_party_evidenceimage_remove_party_uploaded_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidenceimageparty',
            name='evidenceimage',
            field=models.ImageField(null=True, upload_to='evidence_of_payment'),
        ),
    ]
