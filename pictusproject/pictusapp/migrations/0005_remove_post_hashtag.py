# Generated by Django 4.1 on 2022-08-16 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictusapp', '0004_alter_post_hashtag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='hashtag',
        ),
    ]
