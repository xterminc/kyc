# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 11:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incomeexpense', '0001_initial'),
        ('kycform', '0002_personalinfo_house_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='asset_on_colateral',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='incomeexpense.AssetOnCollateral'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='business',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='incomeexpense.Business'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='electronic',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='incomeexpense.Electronic'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='furniture',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='incomeexpense.Furniture'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='loan_detail',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='incomeexpense.LoanDetail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='ornament',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='incomeexpense.Ornament'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='other_asset',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='incomeexpense.OtherAsset'),
            preserve_default=False,
        ),
    ]
