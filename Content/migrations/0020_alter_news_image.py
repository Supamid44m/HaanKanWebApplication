# Generated by Django 4.0 on 2022-12-08 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0019_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(null=True, upload_to='Newsimages'),
        ),
    ]