import time

from django.core.urlresolvers import reverse

from .base import SeleniumTestCase


class MetricsFunctionalTests(SeleniumTestCase):

    def setUp(self):
        super(MetricsFunctionalTests, self).setUp()
        self.login()

    def test_create_metric_save_and_add_another_redirects(self):
        self.get(reverse('metrics:create'))
        create_url = self.selenium.current_url

        self.selenium.save_screenshot("screenshot.png")
        metric_name = self.selenium.find_element_by_id('id_name')
        metric_name.send_keys('Test Metric')
        daily = self.selenium.find_element_by_id("id_daily")
        daily.click()
        description_worst = self.selenium.find_element_by_id('id_description_worst')
        description_worst.send_keys("worst day ever")
        description_best = self.selenium.find_element_by_id('id_description_best')
        description_best.send_keys("best day ever")
        submit_and_add_another_button = self.selenium.find_element_by_name("_save_and_add_another")
        submit_and_add_another_button.click()
        # Metric name should be cleared
        metric_name = self.selenium.find_element_by_id('id_name')
        assert metric_name.get_attribute('value') == ''

        # We're redirected back to the form
        assert self.selenium.current_url == create_url
