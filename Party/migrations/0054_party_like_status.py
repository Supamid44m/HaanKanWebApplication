# Generated by Django 4.0 on 2023-01-28 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Party', '0053_party_dislikes'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='like_status',
            field=models.CharField(default='neutral', max_length=10),
        ),
    ]
