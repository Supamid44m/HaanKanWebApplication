# Generated by Django 4.0 on 2023-01-27 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Party', '0050_party_image_height_party_image_width_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='qrcodeImage',
            field=models.ImageField(height_field='image_height', null=True, upload_to='Partyqrcode', width_field='image_width'),
        ),
    ]
