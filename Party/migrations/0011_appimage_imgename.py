# Generated by Django 4.0 on 2022-12-04 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Party', '0010_rename_qrcodeimagelink_qrcodepayment_qrcodeimageurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='appimage',
            name='imgeName',
            field=models.CharField(max_length=500, null=True),
        ),
    ]