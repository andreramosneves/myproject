# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=255)),
                ('senha', models.CharField(max_length=255)),
            ],
        ),
    ]
