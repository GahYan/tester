# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-30 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0012_auto_20170830_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='mood',
            field=models.IntegerField(choices=[(0, 'Soft'), (1, 'Intense'), (2, 'Rough')]),
        ),
        migrations.AlterField(
            model_name='video',
            name='topic',
            field=models.IntegerField(choices=[(0, 'Normal Romantic Stuff'), (1, 'BDSM'), (2, 'Toys and Machines'), (3, 'Blowjob'), (4, 'Anal'), (5, 'Female Masturbation'), (6, 'Other')]),
        ),
    ]
