import os

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

    def get(self, url):
        return self.selenium.get('%s%s' % (self.live_server_url, url))

    def circleci_screenshot(self, name="screenshot.png"):
        circle_dir = os.environ.get('CIRCLE_ARTIFACTS')
        assert circle_dir, "Could not find CIRCLE_ARTIFACTS environment variable!"
        self.selenium.get_screenshot_as_file(os.path.join(circle_dir, name))
