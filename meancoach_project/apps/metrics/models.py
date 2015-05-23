import datetime
from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models


class Metric(models.Model):
    creator = models.ForeignKey(User, related_name="metrics")
    name = models.CharField(max_length=100)
    description_worst = models.TextField(help_text="eg for measuring Happiness: 'got beat up at school'", verbose_name="Description of the worst ever day of this metric")
    description_best = models.TextField(help_text="eg for measuring Happiness: 'accomplished more than I imagined'", verbose_name="Description of your best ever day of this metric")
    daily = models.BooleanField(default=False, help_text="every day")
    monthly = models.BooleanField(default=False, help_text="every month")
    boolean = models.BooleanField(default=False, help_text="did or didn't (not a 0-10 measurement)")

    def average_span(self, day_span=30):
        avg = Measurement.objects.filter(
            metric=self,
            datetime__gt=datetime.datetime.today() - timedelta(days=day_span),
            datetime__lt=datetime.datetime.today()
        ).aggregate(models.Avg('measurement'))
        return avg['measurement__avg']

    def __unicode__(self):
        if self.daily:
            how_often = "daily"
        else:
            how_often = "monthly"

        if self.boolean:
            boolean_string = "boolean"
        else:
            boolean_string = ""

        return "%s (%s) %s" % (self.name, how_often, boolean_string)


class Measurement(models.Model):
    metric = models.ForeignKey(Metric, unique_for_date="when")
    when = models.DateField()
    measurement = models.IntegerField(default=5, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = (("metric", "when"),)

    def save(self, *args, **kwargs):
        # Boolean should default to 0, not 5!
        if self.pk is None and self.metric.boolean and not self.measurement:
            self.measurement = 0
        if self.metric.monthly and self.when.day != 1:
            raise ValueError("Cannot create a metric record not on the first day of the month!")

        super(Measurement, self).save(*args, **kwargs)

    def __unicode__(self):
        return "Record for %s %s on %s" % (self.measurement, self.metric.name, self.when)
