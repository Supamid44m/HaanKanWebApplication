# Generated by Django 4.0 on 2022-12-10 11:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Party', '0025_rename_partymember_party_partymember'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partymember',
            name='user',
        ),
        migrations.AddField(
            model_name='partymember',
            name='user',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
