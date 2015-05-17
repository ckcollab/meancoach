# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metricrecord',
            old_name='datetime',
            new_name='when',
        ),
        migrations.AlterField(
            model_name='metric',
            name='daily',
            field=models.BooleanField(default=False, help_text=b'every day'),
        ),
        migrations.AlterField(
            model_name='metricrecord',
            name='metric',
            field=models.ForeignKey(to='metrics.Metric', unique_for_date=b'when'),
        ),
    ]
