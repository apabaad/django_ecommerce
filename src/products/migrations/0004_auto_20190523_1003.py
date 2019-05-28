# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-23 04:18
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_filename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='filename',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_img_path),
        ),
    ]