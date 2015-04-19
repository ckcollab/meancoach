from django.core.urlresolvers import reverse
from django.test import TestCase


class TestIndex(TestCase):

    def test_index_page_says_yallo(self):
        resp = self.client.get(reverse('meancoach:index'))
        assert "Yello" in resp.content
