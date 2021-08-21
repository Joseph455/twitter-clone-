# Generated by Django 3.0.9 on 2020-10-09 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweetapp', '0047_auto_20201009_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationinvite',
            name='conversation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tweetapp.Conversation'),
        ),
        migrations.AlterField(
            model_name='conversationinvite',
            name='recipient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invitation_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
