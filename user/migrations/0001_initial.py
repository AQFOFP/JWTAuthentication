# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-08 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
