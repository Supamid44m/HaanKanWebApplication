# Generated by Django 4.0 on 2023-02-03 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Party', '0065_party_like_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='priceaverage',
            field=models.FloatField(default=0.0),
        ),
    ]
