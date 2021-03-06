# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('longitude', models.CharField(blank=True, max_length=250, null=True)),
                ('latitude', models.CharField(blank=True, max_length=250, null=True)),
                ('time', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='image/%Y/%m/%d/%H/%M/%S')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(blank=True, max_length=250, null=True)),
                ('longitude', models.CharField(blank=True, max_length=250, null=True)),
                ('latitude', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, max_length=250, null=True)),
                ('latitude', models.FloatField(blank=True, max_length=250, null=True)),
                ('time', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
