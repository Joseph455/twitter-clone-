# Generated by Django 3.0.8 on 2020-09-08 16:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_like_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='media',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 8, 16, 3, 36, 956953, tzinfo=utc)),
        ),
    ]
