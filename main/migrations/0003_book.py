# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-30 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170330_0731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043d\u0438\u0433\u0438')),
                ('editor', models.CharField(max_length=255, verbose_name='\u0433\u043b\u0430\u0432\u043d\u044b\u0439 \u0440\u0435\u0434\u0430\u043a\u0442\u043e\u0440')),
                ('redaktor', models.CharField(max_length=255, verbose_name='\u0440\u0435\u0434\u0430\u043a\u0442\u043e\u0440')),
                ('prepare', models.CharField(max_length=255, verbose_name='\u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u0438\u043b\u0438')),
                ('description', models.CharField(max_length=255, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('image', models.ImageField(upload_to='', verbose_name='\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430 \u043a\u043d\u0438\u0433\u0438')),
            ],
            options={
                'verbose_name': '\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043a\u043d\u0438\u0433',
                'verbose_name_plural': '\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043a\u043d\u0438\u0433',
            },
        ),
    ]