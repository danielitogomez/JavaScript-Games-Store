# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-07 13:55
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awsomeProject', '0008_auto_20170207_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]