from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from .base import SeleniumTestCase


class MetricsFunctionalTests(SeleniumTestCase):

    def setUp(self):
        super(MetricsFunctionalTests, self).setUp()

        self.user = User.objects.create_user(username="test", password="pass")

        self.get(reverse("account_login"))

        username_input = self.selenium.find_element_by_id('id_login')
        username_input.send_keys("test")
        password_input = self.selenium.find_element_by_id('id_password')
        password_input.send_keys("pass")
        submit_button = self.selenium.find_element_by_css_selector('button[type="submit"]')
        submit_button.click()

    def test_create_metric_save_and_add_another_redirects(self):
        self.get(reverse('metrics:create'))
        create_url = self.selenium.current_url

        metric_name = self.selenium.find_element_by_id('id_name')
        metric_name.send_keys('Test Metric')
        submit_and_add_another_button = self.selenium.find_element_by_name("_save_and_add_another")
        submit_and_add_another_button.click()

        # Metric name should be cleared
        metric_name = self.selenium.find_element_by_id('id_name')
        assert metric_name.get_attribute('value') == ''

        # We're redirected back to the form
        assert self.selenium.current_url == create_url
