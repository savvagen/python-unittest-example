#! /usr/bin/env python
# -*- coding: utf-8 -*-

from object.test_base import TestBase
from object.pages.pages import SearchPage


class SearchTests(TestBase):

    def test_search(self):
        search_results = SearchPage(self.driver).open().search("Selenium")
        self.assertEqual(10, len(search_results._results()))
        self.assertIn("Selenium", search_results._get_result_title(1))

