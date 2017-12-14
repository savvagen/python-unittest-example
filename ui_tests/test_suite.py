import unittest
from ui_tests.search_tests import SearchTests
from ui_tests.login_tests import LoginTests

# get all ui_tests from SearchProductTest and HomePageTest class
search_tests = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])
# run the suite
unittest.TextTestRunner(verbosity=2).run(smoke_tests)