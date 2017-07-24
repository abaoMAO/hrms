# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-09 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='education',
            field=models.CharField(choices=[('1', '\u672c\u79d1'), ('2', '\u7814\u7a76\u751f'), ('3', '\u535a\u58eb')], default='\u672c\u79d1', max_length=10, verbose_name='\u5b66\u5386'),
        ),
        migrations.AddField(
            model_name='staff',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='\u7535\u5b50\u90ae\u7bb1'),
        ),
        migrations.AddField(
            model_name='staff',
            name='political_status',
            field=models.CharField(choices=[('1', '\u7fa4\u4f17'), ('2', '\u56e2\u5458'), ('3', '\u9884\u5907\u515a\u5458'), ('4', '\u515a\u5458')], default='\u56e2\u5458', max_length=10, verbose_name='\u653f\u6cbb\u9762\u8c8c'),
        ),
        migrations.AddField(
            model_name='staff',
            name='qq',
            field=models.IntegerField(blank=True, null=True, verbose_name='QQ\u53f7'),
        ),
        migrations.AddField(
            model_name='staff',
            name='staff_status',
            field=models.CharField(choices=[('1', '\u5728\u804c'), ('2', '\u79bb\u804c'), ('3', '\u5b9e\u4e60')], default='\u5728\u804c', max_length=10, verbose_name='\u804c\u5458\u72b6\u6001'),
        ),
        migrations.AddField(
            model_name='staff',
            name='staff_type',
            field=models.CharField(choices=[('1', '\u5168\u804c'), ('2', '\u517c\u804c')], default='\u5168\u804c', max_length=5, verbose_name='\u804c\u5458\u7c7b\u578b'),
        ),
    ]
