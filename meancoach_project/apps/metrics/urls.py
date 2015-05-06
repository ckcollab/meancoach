import views

from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    # Metrics
    url(r'create/$', views.MetricCreateView.as_view(), name='create'),
    url(r'list/$', views.MetricListView.as_view(), name='list'),
    url(r'delete/(?P<pk>\d+)/$', views.MetricDeleteView.as_view(), name='delete'),
    url(r'update/(?P<pk>\d+)/$', views.MetricUpdateView.as_view(), name='update'),

    # Metric Records
    url(r'input', TemplateView.as_view(template_name='metric_record/input.html'), name='input')
]
