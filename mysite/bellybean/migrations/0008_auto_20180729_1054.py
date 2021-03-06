# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-29 10:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bellybean', '0007_auto_20180728_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.AddField(
            model_name='order',
            name='dish_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bellybean.Dish', blank=True, null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bellybean.Restaurant', blank=True, null=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='item_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
