# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 06:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0002_auto_20170115_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bathroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bathroom_type', models.CharField(choices=[('Pee', 'Pee'), ('Poop', 'Poop')], max_length=3)),
                ('bathroom_time', models.TimeField(default=django.utils.timezone.now)),
                ('bathroom_date', models.DateField(default=datetime.date.today)),
                ('comments', models.TextField(blank=True)),
                ('pet', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pets.Pet')),
            ],
        ),
    ]