from django import forms

from .models import Metric, MetricRecord


class MetricForm(forms.ModelForm):
    class Meta:
        model = Metric
        fields = (
            'name',
            'description_worst',
            'description_best',
            'daily',
            'monthly',
            'boolean',
        )

    def clean(self):
        cleaned_data = super(MetricForm, self).clean()

        if not cleaned_data['daily'] and not cleaned_data['monthly']:
            raise forms.ValidationError("Please select daily or monthly")
        elif cleaned_data['daily'] and cleaned_data['monthly']:
            raise forms.ValidationError("Cannot be both daily and monthly, "
                                        "choose one or the other")

        return cleaned_data


class MetricRecordForm(forms.ModelForm):
    class Meta:
        model = MetricRecord
        fields = (
            'metric',
            'datetime',
            'measurement',
            'notes',
        )
