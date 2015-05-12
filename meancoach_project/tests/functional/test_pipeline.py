from django.core.urlresolvers import reverse
from django.test.utils import override_settings

from .base import SeleniumTestCase


class PipelineFunctionalTest(SeleniumTestCase):

    # Ensure we have production settings for this test
    @override_settings(DEBUG=False)
    @override_settings(ALLOWED_HOSTS=['*'])
    def test_pipeline_compiles_javascript_properly(self):
        self.get(reverse('meancoach:index'))
        link = self.selenium.find_element_by_css_selector(".dropdown-toggle")
        link.click()
        dropdown_link = self.selenium.find_element_by_css_selector(".dropdown-menu")
        assert dropdown_link.is_displayed(), "Couldn't find dropdown menu after clicking dropdown" \
                                             ", javascript probably not working"
