# Generated by Django 3.0.8 on 2020-09-10 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0014_auto_20200909_0936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='user',
            new_name='profile',
        ),
        migrations.RenameField(
            model_name='media',
            old_name='owner',
            new_name='profile',
        ),
    ]
