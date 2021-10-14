import sys
import allure
sys.path.append(sys.path[0] + "/...")

import os
#Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())

from TestData.TestData import TestData
from Pages.Pages import LoginPage
from Utils.WebDriverSetup import WebDriverSetup

import unittest


@allure.title('Test Login Page')
@allure.story('Test_Login_Page')
class Test_Login_Page(WebDriverSetup, TestData):
    def setUp(self):
        super().setUp()
        self.page = LoginPage(self.driver)

    @allure.step
    def base_test(self, result, data_compare):
        print(result)
        self.assertEqual(data_compare, result)

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_blank(self):
        return self.base_test(self.page.login_step(self.NULL,self.NULL), self.MSG_USER_BLANK)
        # self.loginpage=LoginPage(self.driver)
        # error = self.loginpage.login_step(TestData.NULL,TestData.NULL)
        # print(error)
        # self.assertEqual(TestData.MSG_USER_BLANK, error)
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_password_blank(self):
        return self.base_test(self.page.login_step(self.STANDARD_USER,self.NULL), self.MSG_PASS_BLANK)
    #     self.loginpage=LoginPage(self.driver)
    #     error = self.loginpage.login_fail(TestData.STANDARD_USER,TestData.NULL)
    #     self.assertIn(TestData.MSG_PASS_BLANK, error)

    @allure.severity(allure.severity_level.NORMAL)
    def test_login_wrong_username(self):
        return self.base_test(self.page.login_step(self.PASSWORD,self.PASSWORD), self.MSG_WRONG_ACC)
    #     self.loginpage=LoginPage(self.driver)
    #     error = self.loginpage.login_fail(TestData.PASSWORD,TestData.PASSWORD)
    #     self.assertIn(TestData.MSG_WRONG_ACC, error)

    @allure.severity(allure.severity_level.NORMAL)
    def test_login_wrong_password(self):
        return self.base_test(self.page.login_step(self.STANDARD_USER,self.STANDARD_USER), self.MSG_WRONG_ACC)
    #     self.loginpage=LoginPage(self.driver)
    #     error = self.loginpage.login_fail(TestData.STANDARD_USER,TestData.STANDARD_USER)
    #     self.assertIn(TestData.MSG_WRONG_ACC, error)

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_locked_out_user(self):
        return self.base_test(self.page.login_step(self.LOCKED_OUT_USER,self.PASSWORD), self.MSG_LOCKED_OUT_USER)
    #     self.loginpage=LoginPage(self.driver)
    #     error = self.loginpage.login_fail(TestData.LOCKED_OUT_USER,TestData.PASSWORD)
    #     self.assertIn(TestData.MSG_LOCKED_OUT_USER, error)

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_standard_user(self):
        return self.base_test(self.page.login_step(self.STANDARD_USER,TestData.PASSWORD), self.HOME_PAGE_URL)
        # self.loginpage=LoginPage(self.driver)
        # web_link = self.loginpage.login_step(TestData.STANDARD_USER,TestData.PASSWORD)
        # self.assertIn(TestData.HOME_PAGE_URL, web_link)

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_problem_user(self):
        return self.base_test(self.page.login_step(self.PROBLEM_USER,TestData.PASSWORD), self.HOME_PAGE_URL)
        # self.loginpage=LoginPage(self.driver)
        # web_link = self.loginpage.login_success(TestData.PROBLEM_USER,TestData.PASSWORD)
        # self.assertIn(TestData.HOME_PAGE_URL, web_link)
    
    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_performance_glitch_user(self):
        return self.base_test(self.page.login_step(self.PERFORMANCE_GLITCH_USER,TestData.PASSWORD), self.HOME_PAGE_URL)
    #     self.loginpage=LoginPage(self.driver)
    #     web_link = self.loginpage.login_success(TestData.PERFORMANCE_GLITCH_USER,TestData.PASSWORD)
    #     self.assertIn(TestData.HOME_PAGE_URL, web_link)
    

if __name__ == '__main__':
    unittest.main()
