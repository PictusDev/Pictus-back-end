# Generated by Django 4.1 on 2022-08-16 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictusapp', '0003_alter_post_hashtag_alter_post_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hashtag',
            field=models.ManyToManyField(blank=True, to='pictusapp.hashtag'),
        ),
    ]
