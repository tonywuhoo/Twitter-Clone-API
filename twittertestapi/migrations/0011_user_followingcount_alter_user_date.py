# Generated by Django 4.1.3 on 2022-11-21 20:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twittertestapi', '0010_remove_user_followercount_remove_user_followingcount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followingCount',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='Date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2022, 11, 21, 20, 46, 56, 595565)),
        ),
    ]
