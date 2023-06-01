# Generated by Django 4.0 on 2023-03-04 18:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Party', '0072_alter_party_pending_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='party',
            name='pending_members',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
