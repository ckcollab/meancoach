# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0003_auto_20150517_0315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateField()),
                ('measurement', models.IntegerField(default=5, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('metric', models.ForeignKey(to='metrics.Metric', unique_for_date=b'when')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='metricrecord',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='metricrecord',
            name='metric',
        ),
        migrations.DeleteModel(
            name='MetricRecord',
        ),
        migrations.AlterUniqueTogether(
            name='measurement',
            unique_together=set([('metric', 'when')]),
        ),
    ]
