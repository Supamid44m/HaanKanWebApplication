# Generated by Django 4.0 on 2022-12-10 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Party', '0031_alter_party_attendess'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='attendess',
        ),
    ]
