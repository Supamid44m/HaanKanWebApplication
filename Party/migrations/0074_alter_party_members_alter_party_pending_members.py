# Generated by Django 4.0 on 2023-03-04 18:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Party', '0073_alter_party_members_alter_party_pending_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='party',
            name='pending_members',
            field=models.ManyToManyField(null=True, related_name='pending_member', to=settings.AUTH_USER_MODEL),
        ),
    ]
