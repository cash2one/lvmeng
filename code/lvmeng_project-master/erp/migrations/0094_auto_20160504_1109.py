# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields
import django.core.exceptions


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0093_auto_20160504_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='picture',
            field=image_cropping.fields.ImageCropField(blank=True, upload_to=b'business/pictures/', null=True, verbose_name='\u673a\u6784\u516c\u544a\u56fe\u7247(\u5c3a\u5bf8\u5927\u5c0f:375*106)', validators=[django.core.exceptions.ValidationError]),
        ),
    ]
