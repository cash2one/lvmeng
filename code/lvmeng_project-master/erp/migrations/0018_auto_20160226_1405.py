# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0017_agent_entry_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe7\x94\xa8\xe6\x88\xb7'),
        ),
    ]
