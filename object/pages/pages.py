#! /usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from object.user import User

email_field = "input[type='email']"
password_field = "input[type='password']"
next_button = "//span[contains(text(), 'Далее')]"
account_button = "//*[@id='gb']/div[1]/div[1]/div[2]/div[5]/div[1]/a"
logout_button = "//*/a[contains(text(), 'Выйти')]"
email_error = "//*[@id='view_container']/form/div[2]/div/div[1]/div[1]/div/div[2]/div[2]"
password_error = "//*[@id='password']/div[2]/div[2]"

search_field = "q"
search_results = ".srg .g"
search_result_link = "h3 a"


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _email_field(self):
        return self.driver.find_element_by_css_selector(email_field)

    def _password_field(self):
        return self.driver.find_element_by_css_selector(password_field)

    def _next_button(self):
        return self.driver.find_element_by_xpath(next_button)

    def _email_error(self):
        return self.driver.find_element_by_xpath(email_error)

    def _password_error(self):
        return self.driver.find_element_by_xpath(password_error)

    def open(self):
        self.driver.get("https://gmail.com")
        return self

    def login_as(self, user):
        self._email_field().send_keys(user.email, Keys.ENTER)
        self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, password_field)))
        self._password_field().send_keys(user.password, Keys.ENTER)
        return MainPage(self.driver)

    def set_email(self, email):
        self._email_field().send_keys(email, Keys.ENTER)
        self.wait.until(expected_conditions.visibility_of(self._email_error()))
        return self

    def login(self, email, password):
        self._email_field().send_keys(email, Keys.ENTER)
        self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, password_field)))
        self._password_field().send_keys(password, Keys.ENTER)
        self.wait.until(expected_conditions.visibility_of(self._password_error()))
        return self


class MainPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://mail.google.com/mail/#inbox"

    def _account_button(self):
        return self.driver.find_element_by_xpath(account_button)

    def _logout_button(self):
        return self.driver.find_element_by_xpath(logout_button)

    def logout(self):
        self._account_button().click()
        self.wait.until(expected_conditions.visibility_of(self._logout_button()))
        self._logout_button().click()
        return LoginPage(self.driver)


class SearchPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://google.com"

    def open(self):
        self.driver.get(self.url)
        return self

    def _search_field(self):
        return self.driver.find_element_by_name(search_field)

    def search(self, text):
        self._search_field().send_keys(text, Keys.ENTER)
        return SearchResults(self.driver)


class SearchResults(object):
    def __init__(self, driver):
        self.driver = driver

    def _results(self):
        return self.driver.find_elements_by_css_selector(search_results)

    def _get_result_title(self, number):
        results = self._results()[number - 1]
        return results.find_element_by_css_selector(search_result_link).text
        # for result in results:
        #     return result.find_element_by_css_selector(search_result_link).text
