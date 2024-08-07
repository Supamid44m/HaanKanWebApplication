# Generated by Django 4.0 on 2023-01-28 11:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Party', '0051_alter_party_qrcodeimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_parties', to=settings.AUTH_USER_MODEL),
        ),
    ]
