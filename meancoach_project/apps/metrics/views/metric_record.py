import datetime
import json

from dateutil import parser

from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, render

from ..models import Metric, MetricRecord


def make_metric_record_jsonable(metric_record):
    return {
        "name": metric_record.metric.name,
        "metric_id": metric_record.pk,
        "measurement": metric_record.measurement,
        "notes": metric_record.notes,
    }


@login_required()
def metric_record_input(request):
    date_string = request.GET.get('date', None)
    if date_string is not None and date_string is not '':
        date = parser.parse(date_string)
    else:
        date = datetime.date.today()

    metrics = Metric.objects.all()
    if date.day != 1:
        # Not first day of month, so filter out monthly
        metrics = Metric.objects.filter(daily=True, monthly=False)

    metric_records = [MetricRecord.objects.get_or_create(datetime=date, metric=m)[0] for m in metrics]
    metric_records_pks = [m.pk for m in metric_records]

    if request.method == "POST":
        data = json.loads(request.body)

        for metric_pk, value in data.items():
            # Make sure we aren't editing something we don't mean to, like if we didn't refresh the page since yesterday
            # it will only be working with datetime=today() by default
            if int(metric_pk) in metric_records_pks:
                for m in metric_records:
                    if m.pk == int(metric_pk):
                        m.notes = value.get('notes', None)
                        m.measurement = value['measurement']
                        m.save()

        return HttpResponse(status=200)

    daily_checklist = []
    daily_entries = []
    monthly_entries = []

    for m in metric_records:
        jsond_metric_model = make_metric_record_jsonable(m)
        if m.metric.daily and m.metric.boolean:
            daily_checklist.append(jsond_metric_model)
        elif m.metric.daily and not m.metric.boolean:
            daily_entries.append(jsond_metric_model)
        elif m.metric.monthly:
            monthly_entries.append(jsond_metric_model)

    context = {
        "javascript_context_holder": json.dumps({
            'daily_checklist': daily_checklist,
            'daily_entries': daily_entries,
            'monthly_entries': monthly_entries,
            'day_of_month': date.day,
            'date': str(date),
        })
    }

    if request.is_ajax():
        return HttpResponse(json.dumps(context['javascript_context_holder']))
    else:
        return render(request, 'metric_record/input.html', context)
