# Generated by Django 4.0 on 2023-02-27 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0027_alter_news_desciption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='desciption',
            field=models.TextField(blank=True, max_length=100000, null=True),
        ),
    ]
