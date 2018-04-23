# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fav_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Follows',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('id_user', models.IntegerField()),
                ('following_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Retweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('id_user', models.IntegerField()),
                ('twt_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('id_user', models.IntegerField()),
                ('content', models.CharField(max_length=280)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user_id', models.IntegerField()),
                ('fn', models.CharField(max_length=25)),
                ('ln', models.CharField(max_length=25)),
                ('twitter_handle', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='retweet',
            name='tweet_id',
            field=models.ForeignKey(to='twitter_app.Tweets'),
        ),
        migrations.AddField(
            model_name='retweet',
            name='user_tweet',
            field=models.ForeignKey(to='twitter_app.User'),
        ),
        migrations.AddField(
            model_name='follows',
            name='user_fllw',
            field=models.ForeignKey(to='twitter_app.User'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='twt_id',
            field=models.ForeignKey(to='twitter_app.Tweets'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user_twt',
            field=models.ForeignKey(to='twitter_app.User'),
        ),
    ]
