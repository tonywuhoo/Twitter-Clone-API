# Generated by Django 4.1.3 on 2022-11-22 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twittertestapi', '0022_alter_comment_ownerid_alter_comment_postid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followerList',
        ),
        migrations.AddField(
            model_name='user',
            name='followerList',
            field=models.ManyToManyField(blank=True, to='twittertestapi.user'),
        ),
    ]
