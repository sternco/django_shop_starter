# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('product_des', models.CharField(max_length=400)),
                ('product_price', models.CharField(max_length=10)),
            ],
        ),
    ]
