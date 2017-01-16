# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 05:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0002_auto_20170115_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feeding_time', models.TimeField(default=datetime.datetime(2017, 1, 16, 5, 24, 4, 765249, tzinfo=utc))),
                ('feeding_date', models.DateField(default=datetime.date.today)),
                ('comments', models.TextField(blank=True)),
                ('pet', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pets.Pet')),
            ],
        ),
    ]
