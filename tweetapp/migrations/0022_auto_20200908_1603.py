# Generated by Django 3.0.8 on 2020-09-08 16:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tweetapp', '0021_auto_20200908_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
