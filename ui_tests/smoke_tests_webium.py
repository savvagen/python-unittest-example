#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from object.pages_webium.pages import LoginPage
from object.user import User


class SmokeTestsWebium(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(10)

    def test_login(self):
        user = User('genchevskiy', 'test')
        main_page = LoginPage(self.driver).open().login_as(user)
        main_page.wait.until(lambda: main_page.account_button)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
