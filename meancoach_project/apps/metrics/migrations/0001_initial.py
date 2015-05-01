# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description_worst', models.TextField(null=True, blank=True)),
                ('description_best', models.TextField(null=True, blank=True)),
                ('daily', models.BooleanField(default=True, help_text=b'every day')),
                ('monthly', models.BooleanField(default=False, help_text=b'every month')),
                ('boolean', models.BooleanField(default=False, help_text=b"did or didn't (not a 0-10 measurement)")),
                ('creator', models.ForeignKey(related_name='metrics', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MetricRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateField()),
                ('measurement', models.IntegerField(default=5, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('metric', models.ForeignKey(to='metrics.Metric', unique_for_date=b'datetime')),
            ],
        ),
    ]
