from django.core.urlresolvers import reverse

from .base import SeleniumTestCase


class IndexFunctionalTest(SeleniumTestCase):

    def test_index_yello_in_da_house(self):
        self.get(reverse('meancoach:index'))
        assert self.selenium.find_element_by_id('yello_h1_in_da_house')
