# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metingen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='nha_nr',
            field=models.CharField(max_length=15, null=True),
        ),
    ]