# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-14 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awsomeProject', '0011_auto_20170214_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(default=b'', max_length=300),
        ),
    ]
