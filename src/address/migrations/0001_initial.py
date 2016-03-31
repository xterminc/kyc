# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaitiAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('zone', models.CharField(choices=[('mechi', 'Mechi'), ('bagmait', 'Bagmati')], default='Lumbini', max_length=100)),
                ('district', models.CharField(choices=[('gulmi', 'Gulmi')], default='gulmi', max_length=100)),
                ('vdc', models.CharField(max_length=100)),
                ('ward_no', models.IntegerField(default=1)),
                ('house_no', models.IntegerField(default=0)),
                ('street', models.CharField(max_length=100)),
                ('tel_no', models.IntegerField()),
                ('pobox_no', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PermanentAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('zone', models.CharField(choices=[('mechi', 'Mechi'), ('bagmait', 'Bagmati')], default='Lumbini', max_length=100)),
                ('district', models.CharField(choices=[('gulmi', 'Gulmi')], default='gulmi', max_length=100)),
                ('vdc', models.CharField(max_length=100)),
                ('ward_no', models.IntegerField(default=1)),
                ('house_no', models.IntegerField(default=0)),
                ('street', models.CharField(max_length=100)),
                ('tel_no', models.IntegerField()),
                ('pobox_no', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TemporaryAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('zone', models.CharField(choices=[('mechi', 'Mechi'), ('bagmait', 'Bagmati')], default='Lumbini', max_length=100)),
                ('district', models.CharField(choices=[('gulmi', 'Gulmi')], default='gulmi', max_length=100)),
                ('vdc', models.CharField(max_length=100)),
                ('ward_no', models.IntegerField(default=1)),
                ('house_no', models.IntegerField(default=0)),
                ('street', models.CharField(max_length=100)),
                ('tel_no', models.IntegerField()),
                ('pobox_no', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
