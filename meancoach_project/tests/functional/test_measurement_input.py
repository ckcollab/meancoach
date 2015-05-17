import time

from datetime import timedelta
from dateutil import parser

from django.core.urlresolvers import reverse

from selenium.webdriver.common.keys import Keys

from .base import SeleniumTestCase

from metrics.models import Metric


class MetricRecordInputFunctionalTest(SeleniumTestCase):

    def setUp(self):
        super(MetricRecordInputFunctionalTest, self).setUp()
        self.metric = Metric.objects.create(creator=self.user,
                                            name="test metric",
                                            daily=True)
        self.login()
        self.get(reverse('metrics:input'))

    def test_metric_input_page_form_is_visible(self):
        # Can we see a measurement input?
        assert self.selenium.find_element_by_name("measurement")

    def test_metric_input_page_back_and_forward_button_changes_page_dates(self):
        metric_date = self.selenium.find_element_by_css_selector("span.metric_date")
        old_date = parser.parse(metric_date.text)

        previous = self.selenium.find_element_by_css_selector(".day_link.previous")
        previous.click()
        metric_date = self.selenium.find_element_by_css_selector("span.metric_date")
        new_date = parser.parse(metric_date.text)
        assert (new_date - old_date) == timedelta(days=-1)

        next = self.selenium.find_element_by_css_selector(".day_link.next")
        next.click()
        metric_date = self.selenium.find_element_by_css_selector("span.metric_date")
        even_newer_date = parser.parse(metric_date.text)
        assert (even_newer_date - new_date) == timedelta(days=1)

    def test_metric_input_page_saves_data_on_refresh(self):
        input_slider = self.selenium.find_element_by_css_selector('input[type="range"]')
        # Change the value to 4
        input_slider.send_keys(Keys.ARROW_LEFT)
        textarea = self.selenium.find_element_by_css_selector('textarea')
        textarea.send_keys("Some notes for the test")
        # Let the save happen
        time.sleep(3)
        self.get(reverse('metrics:input'))
        input_slider = self.selenium.find_element_by_css_selector('input[type="range"]')
        textarea = self.selenium.find_element_by_css_selector('textarea')
        assert int(input_slider.get_attribute("value")) == 4
        # using 'in' here because weird formatting for textarea
        assert "Some notes for the test" in textarea.text
