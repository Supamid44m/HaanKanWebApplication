# Generated by Django 4.0 on 2023-02-22 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0024_news_dislikes_news_like_status_news_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
