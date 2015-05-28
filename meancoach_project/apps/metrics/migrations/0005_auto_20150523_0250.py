# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0004_auto_20150517_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metric',
            name='description_best',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='metric',
            name='description_worst',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
