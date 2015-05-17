import os

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import LiveServerTestCase

from selenium.webdriver.phantomjs.webdriver import WebDriver


class SeleniumTestCase(LiveServerTestCase):
    urls = 'urls'

    @classmethod
    def setUpClass(cls):
        super(SeleniumTestCase, cls).setUpClass()
        cls.selenium = WebDriver()
        # Wait 10 seconds for elements to appear, always
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SeleniumTestCase, cls).tearDownClass()

    def setUp(self):
        super(SeleniumTestCase, self).setUp()
        self.selenium.set_window_size(1400, 1000)
        self.user = User.objects.create_user("test", password="test")

    def get(self, url):
        return self.selenium.get('%s%s' % (self.live_server_url, url))

    def login(self):
        self.get(reverse('account_login'))
        username = self.selenium.find_element_by_id("id_login")
        username.send_keys("test")
        password = self.selenium.find_element_by_id("id_password")
        password.send_keys("test")
        submit = self.selenium.find_element_by_css_selector('button[type="submit"]')
        submit.click()

    def circleci_screenshot(self, name="screenshot.png"):
        circle_dir = os.environ.get('CIRCLE_ARTIFACTS')
        assert circle_dir, "Could not find CIRCLE_ARTIFACTS environment variable!"
        self.selenium.get_screenshot_as_file(os.path.join(circle_dir, name))
