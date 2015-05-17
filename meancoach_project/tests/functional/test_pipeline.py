from django.core.urlresolvers import reverse

from .base import SeleniumTestCase


class PipelineFunctionalTest(SeleniumTestCase):

    def test_pipeline_compiles_javascript_properly(self):
        '''For some reason javascript isn't minified properly, ensure that it
        is loaded properly by checking that the dropdown menu is available

        A better way to check may be by failing on _any_ JS error, but I think
        there are errors sometimes that don't cause a critical failure... not
        sure.'''
        self.get(reverse('meancoach:index'))
        link = self.selenium.find_element_by_css_selector(".dropdown-toggle")
        link.click()
        dropdown_link = self.selenium.find_element_by_css_selector(".dropdown-menu")
        assert dropdown_link.is_displayed(), "Couldn't find dropdown menu after clicking dropdown, " \
                                             "javascript probably not working"

    def test_pipeline_compiles_css_properly(self):
        '''Make sure our CSS was included at least well enough to have a
        responsive interface'''
        self.selenium.set_window_size(420, 600)
        self.get(reverse('meancoach:index'))
        assert self.selenium.find_element_by_css_selector('.hamburger_button')
