# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-16 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webgui', '0006_auto_20170716_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leisure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=25, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
