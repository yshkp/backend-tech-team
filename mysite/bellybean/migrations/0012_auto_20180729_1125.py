# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-29 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bellybean', '0011_auto_20180729_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='dish_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dish',
            name='restaurant',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bellybean.Restaurant'),
        ),
        migrations.AlterField(
            model_name='order',
            name='dish_name',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bellybean.Dish'),
        ),
        migrations.AlterField(
            model_name='order',
            name='item_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bellybean.Restaurant'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='rest_name',
            field=models.CharField(default='', max_length=100, verbose_name='Restaurant Name'),
            preserve_default=False,
        ),
    ]
