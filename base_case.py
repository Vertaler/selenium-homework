import os
import unittest

import selenium
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import DesiredCapabilities, Remote

import utils
from pages.auth_page import AuthPage

# firefox_capabilities = DesiredCapabilities.FIREFOX
# firefox_capabilities['marionette'] = True


class BaseCase(unittest.TestCase):

    def setUp(self):
        try:
            self.dummyEnvSet("technopark9", "testQA1")
            browser = os.environ.get('BROWSER', 'FIREFOX')
            self.driver = Remote(
                command_executor='http://127.0.0.1:4444/wd/hub',
                desired_capabilities=getattr(DesiredCapabilities, browser).copy()
            )
            page = AuthPage(self.driver)
            page.open()
            auth_form = page.form
            login = os.environ['LOGIN']
            password = os.environ['PASSWORD']
            auth_form.signin(login, password)
            utils.wait(self.driver, lambda d: not d.title.startswith(page.TITLE))
        except:
            self.driver.quit()
            raise

    def tearDown(self):
        self.driver.quit()

    def dummyEnvSet(self, login, password):
        os.environ['LOGIN'] = login
        os.environ['PASSWORD'] = password
