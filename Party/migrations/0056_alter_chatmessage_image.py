# Generated by Django 4.0 on 2023-01-30 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Party', '0055_chatmessage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Chat-message'),
        ),
    ]