# Generated by Django 3.0.9 on 2020-09-13 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0021_auto_20200913_2215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='creator',
            new_name='profile',
        ),
        migrations.RenameField(
            model_name='media',
            old_name='creator',
            new_name='profile',
        ),
    ]
