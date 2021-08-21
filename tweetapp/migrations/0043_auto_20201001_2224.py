# Generated by Django 3.0.9 on 2020-10-01 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweetapp', '0042_auto_20200922_0140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='image',
            new_name='image-content',
        ),
        migrations.RemoveField(
            model_name='message',
            name='content',
        ),
        migrations.AddField(
            model_name='message',
            name='text-content',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
