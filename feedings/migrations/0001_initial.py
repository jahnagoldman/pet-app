# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-24 08:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('date', models.DateField(default=datetime.date.today)),
                ('comments', models.TextField(blank=True)),
                ('event_type', models.CharField(choices=[('Walk', 'Walk'), ('Bathroom', 'Bathroom'), ('Feeding', 'Feeding'), ('Medicine', 'Medicine')], max_length=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='feedings.Event')),
            ],
            bases=('feedings.event',),
        ),
        migrations.AddField(
            model_name='event',
            name='pet',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pets.Pet'),
        ),
    ]
