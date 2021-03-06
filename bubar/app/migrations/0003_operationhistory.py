# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-12-27 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201227_0346'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flow_type', models.CharField(max_length=10, verbose_name='流类型')),
                ('project_name', models.CharField(max_length=100, verbose_name='项目名称')),
                ('operator', models.CharField(max_length=100, verbose_name='操作员')),
                ('data', models.TextField(default={}, verbose_name='操作数据')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
