# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 10:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('housedetail', '0001_initial'),
        ('kycform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='house_detail',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='housedetail.HouseDetail'),
            preserve_default=False,
        ),
    ]
