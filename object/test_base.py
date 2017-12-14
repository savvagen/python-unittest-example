#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from object.pages.pages import MainPage



class TestBase(unittest.TestCase):

    def setUp(self):
        # USING HEADLESS CHROME
        # ---------------------------------------
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--window-size=1920x1080")
        # # download chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
        # # current directory
        # chrome_driver = os.getcwd() + "/chromedriver"
        # self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
        # ---------------------------------------
        # self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(10)

    def tearDown(self):
        if self.driver.current_url == MainPage(self.driver).url:
            MainPage(self.driver).logout()
        self.driver.close()
