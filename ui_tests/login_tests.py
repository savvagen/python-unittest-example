#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest

from ddt import ddt, data, unpack

from object.pages.pages import LoginPage
from object.test_base import TestBase
from object.user import User
from ui_tests.test_data.login_controller import *

cwd = os.path.dirname(os.path.realpath(__file__))
#cwd = os.getcwd()


@ddt
class LoginTests(TestBase):

    def test_login(self):
        user = User('genchevskiy', 'test')
        main_page = LoginPage(self.driver).open().login_as(user)
        self.assertTrue(main_page._account_button().is_displayed())
        self.assertEqual(self.driver.current_url, main_page.url)

    @data(*get_csv_data("{}/test_data/login_data.csv".format(cwd)))
    @unpack
    def test_invalid_email_login(self, email, password, message):
        login_page = LoginPage(self.driver).open().set_email(email)
        self.assertTrue(login_page._email_error().is_displayed())
        self.assertEqual(login_page._email_error().text, message)

    @data(*get_csv_data("{}/test_data/password_data.csv".format(cwd)))
    @unpack
    def test_invalid_password_login(self, email, password, message):
        login_page = LoginPage(self.driver).open().login(email, password)
        self.assertTrue(login_page._password_error().is_displayed())
        self.assertIn(message, login_page._password_error().text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
