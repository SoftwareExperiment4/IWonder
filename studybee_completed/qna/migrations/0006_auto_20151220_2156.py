# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-20 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0005_auto_20150616_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.TextField(),
        ),
    ]
