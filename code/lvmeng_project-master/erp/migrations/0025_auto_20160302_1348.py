# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0024_auto_20160302_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='name',
            field=models.CharField(default=b'', max_length=30, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='business',
            name='name',
            field=models.CharField(default=b'', max_length=50, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default=b'', max_length=30, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d'),
        ),
    ]
