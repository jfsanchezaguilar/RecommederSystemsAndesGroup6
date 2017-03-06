# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecommendApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=200)),
                ('book_title', models.CharField(max_length=200)),
                ('book_author', models.CharField(max_length=200)),
                ('year_publish', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('image_small', models.CharField(max_length=2000)),
                ('image_medium', models.CharField(max_length=2000)),
                ('image_large', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='BookRaiting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('isbn', models.CharField(max_length=200)),
                ('raiting', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BookUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('location', models.CharField(max_length=200, null=True)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
    ]