# Generated by Django 4.0 on 2022-11-30 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('quantity', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
