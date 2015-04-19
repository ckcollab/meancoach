from django.core.urlresolvers import reverse
from django.test import TestCase


class SmokeTestMeanCoach(TestCase):

    def test_index_page_returns_200(self):
        resp = self.client.get(reverse('meancoach:index'))
        assert resp.status_code == 200
