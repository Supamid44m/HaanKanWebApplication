# Generated by Django 4.0 on 2022-12-08 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0007_alter_news_image_delete_newsimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(null=True, upload_to='NewsImage'),
        ),
    ]
