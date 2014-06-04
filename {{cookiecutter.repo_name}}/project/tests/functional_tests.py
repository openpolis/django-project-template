from django.test import LiveServerTestCase
from selenium import webdriver

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_visit_homepage(self):
        # She goes to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn('{{ cookiecutter.project_name }}', self.browser.title)
        self.fail('Finish the test!')
