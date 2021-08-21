# Generated by Django 3.0.8 on 2020-09-10 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweetapp', '0033_auto_20200910_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rep',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='rep',
            name='feed',
        ),
        migrations.RemoveField(
            model_name='rep',
            name='message',
        ),
        migrations.RemoveField(
            model_name='rep',
            name='reply',
        ),
        migrations.AlterField(
            model_name='reply',
            name='message',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='tweetapp.Message'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='tweet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_set', to='tweetapp.Tweet'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tweet_set', to='tweetapp.Tweet'),
        ),
        migrations.DeleteModel(
            name='Feed',
        ),
        migrations.DeleteModel(
            name='Rep',
        ),
    ]
