# Generated by Django 3.0.8 on 2020-09-10 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweetapp', '0027_auto_20200909_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='was_retweeted',
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Rep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rep', related_query_name='rep_set', to='tweetapp.Rep')),
                ('message', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tweetapp.Message')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feed', related_query_name='feed_set', to='tweetapp.Feed')),
                ('message', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tweetapp.Message')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
