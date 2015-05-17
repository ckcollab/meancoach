from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# from django.test.utils import override_settings

from tests.functional.base import SeleniumTestCase

from ..models import Metric  # , Measurement


class MetricRecordInputFunctionalTest(SeleniumTestCase):

    def setUp(self):
        super(MetricRecordInputFunctionalTest, self).setUp()
        self.user = User.objects.create_user("test", password="test")
        self.metric = Metric.objects.create(creator=self.user,
                                            name="test metric",
                                            daily=True)

        self.get(reverse('account_login'))
        username = self.selenium.find_element_by_id("id_login")
        username.send_keys("test")
        password = self.selenium.find_element_by_id("id_password")
        password.send_keys("test")
        submit = self.selenium.find_element_by_css_selector('button[type="submit"]')
        submit.click()

        self.get(reverse('metrics:input'))

        self.selenium.save_screenshot('screenshot.png')

    # Ensure we have production settings for this test so the js files are
    # minified (could cause problems not seen in dev)
    # @override_settings(DEBUG=False)
    # @override_settings(ALLOWED_HOSTS=['*'])
    # def test_metric_input_page_form_is_visible(self):
    #     # create user
    #     # create metric
    #     # go to metric input page
    #     # see metric input form
    #     assert False
