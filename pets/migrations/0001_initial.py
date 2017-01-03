# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('pet_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('animal', models.CharField(choices=[('dog', 'DOG'), ('cat', 'CAT')], default='Dog', max_length=3)),
                ('microchip_number', models.CharField(max_length=30)),
            ],
        ),
    ]
