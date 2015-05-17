from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from ..models import Metric


class SmokeTestMetrics(TestCase):
    '''We're testing all of our return status codes here, the simplest
    test possible. Using `self.views` to define each view and the arguments
    passed to it.'''

    def setUp(self):
        self.user = User.objects.create_user("test", password="test")
        self.other_user = User.objects.create_user("other_user", password="test")
        self.metric = Metric.objects.create(creator=self.user, name="test metric")
        self.views = (
            # (view name, object pk used in view)
            ('list', None),
            ('create', None),
            ('update', {'pk': self.metric.pk}),
            ('delete', {'pk': self.metric.pk}),
        )

    def test_metrics_pages_returns_200_logged_in(self):
        for view, kwargs in self.views:
            self.client.login(username="test", password="test")
            resp = self.client.get(reverse('metrics:%s' % view, kwargs=kwargs))
            assert resp.status_code == 200, "metrics:%s view not working for " \
                                            "logged in users" % view

    def test_metrics_pages_returns_302_not_logged_in(self):
        for view, kwargs in self.views:
            resp = self.client.get(reverse('metrics:%s' % view, kwargs=kwargs))
            assert resp.status_code == 302, "metrics:%s view not working for " \
                                            "non logged in users" % view

    def test_metrics_pages_with_object_require_ownership(self):
        for view, kwargs in self.views:
            # Only on views with kwargs (an object passed to them)
            if kwargs:
                # Login as a different user then creator
                self.client.login(username="other_user", password="test")
                resp = self.client.get(reverse('metrics:%s' % view, kwargs=kwargs))
                assert resp.status_code == 404, "metrics:%s view permissions" \
                                                "not being enforced" % view


class SmokeTestMetricRecords(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("test", password="test")

    def test_metric_records_page_returns_200_logged_in(self):
        self.client.login(username="test", password="test")
        resp = self.client.get(reverse('metrics:input'))
        assert resp.status_code == 200

    def test_metric_records_page_returns_302_not_logged_in(self):
        resp = self.client.get(reverse('metrics:input'))
        assert resp.status_code == 302
