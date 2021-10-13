import sys

sys.path.append(sys.path[0] + "/...")

import os
#Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())

from TestData.TestData import TestData
from Pages.Pages import LoginPage
from Utils.WebDriverSetup import WebDriverSetup

import unittest


# Test Class containing all tests
class Test_Login_Page(WebDriverSetup):
    def setUp(self):
        super().setUp()

    def test_login_username_blank(self):
        self.loginpage=LoginPage(self.driver)
        error = self.loginpage.login_fail(TestData.NULL,TestData.NULL)
        print(error)
        self.assertEqual(TestData.MSG_USER_BLANK, error)

    def test_login_password_blank(self):
        self.loginpage=LoginPage(self.driver)
        error = self.loginpage.login_fail(TestData.STANDARD_USER,TestData.NULL)
        self.assertIn(TestData.MSG_PASS_BLANK, error)

    def test_login_wrong_username(self):
        self.loginpage=LoginPage(self.driver)
        error = self.loginpage.login_fail(TestData.PASSWORD,TestData.PASSWORD)
        self.assertIn(TestData.MSG_WRONG_ACC, error)

    def test_login_wrong_password(self):
        self.loginpage=LoginPage(self.driver)
        error = self.loginpage.login_fail(TestData.STANDARD_USER,TestData.STANDARD_USER)
        self.assertIn(TestData.MSG_WRONG_ACC, error)

    def test_login_username_locked_out_user(self):
        self.loginpage=LoginPage(self.driver)
        error = self.loginpage.login_fail(TestData.LOCKED_OUT_USER,TestData.PASSWORD)
        self.assertIn(TestData.MSG_LOCKED_OUT_USER, error)

    def test_login_username_standard_user(self):
        self.loginpage=LoginPage(self.driver)
        web_link = self.loginpage.login_success(TestData.STANDARD_USER,TestData.PASSWORD)
        self.assertIn(TestData.HOME_PAGE_URL, web_link)

    def test_login_username_problem_user(self):
        self.loginpage=LoginPage(self.driver)
        web_link = self.loginpage.login_success(TestData.PROBLEM_USER,TestData.PASSWORD)
        self.assertIn(TestData.HOME_PAGE_URL, web_link)
    #
    def test_login_username_performance_glitch_user(self):
        self.loginpage=LoginPage(self.driver)
        web_link = self.loginpage.login_success(TestData.PERFORMANCE_GLITCH_USER,TestData.PASSWORD)
        self.assertIn(TestData.HOME_PAGE_URL, web_link)
    #
    def test_login_username_performance_glitch_user_Failed(self):
        self.loginpage=LoginPage(self.driver)
        web_link = self.loginpage.login_success(TestData.PERFORMANCE_GLITCH_USER,TestData.PASSWORD)
        self.assertIn(TestData.HOME_PAGE_URL, web_links)

if __name__ == '__main__':
    unittest.main()
