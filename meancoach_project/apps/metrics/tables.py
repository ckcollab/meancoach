import django_tables2 as tables

from .models import Metric


class MetricTable(tables.Table):
    update = tables.TemplateColumn(template_name="metric/_update_row.html",
                                   sortable=False)
    delete = tables.TemplateColumn(template_name="metric/_delete_row.html",
                                   sortable=False)

    class Meta:
        model = Metric
        attrs = {"class": "table table-striped"}
        fields = (
            'name',
            'daily',
            'monthly',
            'boolean',
        )
        sequence = (
            'update',
            'delete',
            'name',
            'daily',
            'monthly',
            'boolean',
        )
