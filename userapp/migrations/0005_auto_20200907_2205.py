# Generated by Django 3.0.8 on 2020-09-07 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_auto_20200907_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.Profile'),
        ),
    ]
