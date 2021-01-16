# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-02 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_operationhistory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operationhistory',
            options={'verbose_name': '操作历史', 'verbose_name_plural': '操作历史'},
        ),
        migrations.AddField(
            model_name='operationhistory',
            name='result',
            field=models.TextField(default={}, verbose_name='结果'),
        ),
        migrations.AlterField(
            model_name='operationhistory',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='操作时间'),
        ),
    ]