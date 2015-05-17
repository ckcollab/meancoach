from django.contrib import admin
from .models import Metric, Measurement

admin.site.register(Metric)
admin.site.register(Measurement)
