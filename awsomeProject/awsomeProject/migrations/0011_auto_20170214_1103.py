# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-14 09:03
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('awsomeProject', '0010_merge_20170207_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='category',
            field=models.CharField(choices=[(b'Action', b'Action'), (b'Advanture', b'Adventure'), (b'Sports', b'Sports'), (b'Strategy', b'Strategy')], default=b'Action', max_length=20),
        ),
        migrations.AddField(
            model_name='game',
            name='created',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name=b'image'),
        ),
    ]
