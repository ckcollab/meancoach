import random

from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from metrics.models import Metric, MetricRecord


class Command(BaseCommand):
    help = 'Generate data for development (local/staging) environments'

    def handle(self, *args, **options):
        try:
            admin = User.objects.get(username="admin")
        except User.DoesNotExist:
            admin = User.objects.create_superuser("admin", "admin@test.com", "pass")

        premade_metrics = [
            # Daily
            {
                "name": "Happiness",
                "description_worst": "Got beat up at school",
                "description_best": "Got first place in the big race",
                "daily": True,
            },
            {
                "name": "Strength",
                "description_worst": "Sat on the couch dreaming about the gym",
                "description_best": "Got a personal record in every lift",
                "daily": True,
            },
            # Daily checklist
            {
                "name": "Ate vitamins",
                "daily": True,
                "boolean": True,
            },
            # Monthly
            {
                "name": "Nature",
                "description_worst": "Didn't go outside all month",
                "description_best": "Every opportunity to enjoy nature was taken",
                "monthly": True,
            },
        ]

        for metric_kwargs in premade_metrics:
            metric = Metric.objects.create(creator=admin, **metric_kwargs)

            # For today and 30 days in the past add some records
            for n in range(30):
                notes = None
                measurement = 0
                date = datetime.now() - timedelta(days=n)

                if metric.daily or metric.monthly and not metric.boolean:
                    if random.randint(1, 10) % 10 == 0:
                        notes = "Some random note"
                    measurement = random.randint(1, 10)
                elif metric.daily and metric.boolean:
                    # Boolean metrics are either false (0) or true (1)
                    measurement = random.randint(0, 1)

                if metric.monthly and date.day != 1:
                    # Only add monthly metrics on first day of month
                    continue

                MetricRecord.objects.create(
                    metric=metric,
                    datetime=date,
                    measurement=measurement,
                    notes=notes,
                )
