# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-23 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190522_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='filename',
            field=models.FileField(blank=True, null=True, upload_to='products/'),
        ),
    ]
