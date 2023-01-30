# Generated by Django 4.0 on 2023-01-25 04:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Party', '0045_chatmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='paid_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='party',
            name='paid_day',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)]),
        ),
    ]
