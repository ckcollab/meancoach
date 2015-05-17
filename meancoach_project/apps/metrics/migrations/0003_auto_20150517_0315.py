# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0002_auto_20150517_0222'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='metricrecord',
            unique_together=set([('metric', 'when')]),
        ),
    ]
