# Generated by Django 4.1.3 on 2022-11-22 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twittertestapi', '0043_remove_user_followrequestsent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='isUser',
        ),
    ]
