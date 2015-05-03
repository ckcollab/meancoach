from django.core.urlresolvers import reverse
from django.shortcuts import Http404, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, \
    DetailView, ListView

from django_tables2 import SingleTableMixin

from apps.core.views import LoginRequiredMixin
from ..forms import MetricForm, MetricRecordForm
from ..models import Metric, MetricRecord
from ..tables import MetricTable


class MetricViewMixin(object):
    '''This is a helper mixin providing generic support for all of the
    Metric views'''
    model = Metric
    form_class = MetricForm

    def get_object(self, queryset=None):
        obj = super(MetricViewMixin, self).get_object()
        if not obj.creator == self.request.user:
            raise Http404
        return obj

    def get_success_url(self):
        return self.success_url or reverse("metrics:list")


class MetricListView(MetricViewMixin, LoginRequiredMixin, SingleTableMixin, ListView):
    template_name = "metrics/list.html"
    table_class = MetricTable


class MetricDeleteView(MetricViewMixin, LoginRequiredMixin, DeleteView):
    template_name = 'metrics/confirm_delete.html'


class MetricFormMixin(object):

    def check_save_add_another(self, form):
        '''Check if someone clicked "save and add another" and redirect
        when they do'''
        if '_save_and_add_another' in form.data:
            self.success_url = reverse("metrics:create")

        return HttpResponseRedirect(self.get_success_url())


class MetricCreateView(MetricViewMixin, MetricFormMixin, LoginRequiredMixin, CreateView):
    template_name = "metrics/form.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return self.check_save_add_another(form)


class MetricUpdateView(MetricViewMixin, MetricFormMixin, LoginRequiredMixin, UpdateView):
    template_name = "metrics/form.html"

    def form_valid(self, form):
        return self.check_save_add_another(form)
