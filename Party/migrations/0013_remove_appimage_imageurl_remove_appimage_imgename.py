# Generated by Django 4.0 on 2022-12-08 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Party', '0012_remove_party_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appimage',
            name='imageURL',
        ),
        migrations.RemoveField(
            model_name='appimage',
            name='imgeName',
        ),
    ]