# Generated by Django 4.0 on 2023-01-25 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Party', '0046_party_paid_date_party_paid_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='paid_date',
        ),
        migrations.RemoveField(
            model_name='party',
            name='paid_day',
        ),
    ]