# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_auto_20170115_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='animal',
            field=models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat')], max_length=3),
        ),
    ]
