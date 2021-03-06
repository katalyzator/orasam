# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-30 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170330_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='')),
                ('description', models.CharField(max_length=1000, verbose_name='')),
                ('image', models.ImageField(upload_to='', verbose_name='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.AlterModelOptions(
            name='sliderimage',
            options={'verbose_name': '\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430', 'verbose_name_plural': '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430'},
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430'),
        ),
    ]
