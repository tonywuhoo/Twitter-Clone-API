# Generated by Django 4.1.3 on 2022-11-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twittertestapi', '0028_alter_post_ownerid_remove_user_likedposts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followerList',
            field=models.ManyToManyField(blank=True, to='twittertestapi.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='followingList',
            field=models.ManyToManyField(blank=True, to='twittertestapi.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='likedPosts',
            field=models.ManyToManyField(blank=True, to='twittertestapi.post'),
        ),
    ]
