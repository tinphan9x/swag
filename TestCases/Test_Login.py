import sys, os
import allure
import unittest
import pytest
sys.path.append(sys.path[0] + "/...")
#Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())

from TestData.TestData import TestData
from Pages.Pages import LoginPage
from Utils.WebDriverSetup import WebDriverSetup



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

    #@pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_blank(self):
        return self.base_test(self.page.login_step(self.NULL,self.NULL), self.MSG_USER_BLANK)

    @allure.severity(allure.severity_level.NORMAL)
    def test_login_password_blank(self):
        return self.base_test(self.page.login_step(self.STANDARD_USER,self.NULL), self.MSG_PASS_BLANK)

    @allure.severity(allure.severity_level.NORMAL)
    def test_login_wrong_username(self):
        return self.base_test(self.page.login_step(self.PASSWORD,self.PASSWORD), self.MSG_WRONG_ACC)

    @allure.severity(allure.severity_level.NORMAL)
    def test_login_wrong_password(self):
        return self.base_test(self.page.login_step(self.STANDARD_USER,self.STANDARD_USER), self.MSG_WRONG_ACC)

    #@pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_locked_out_user(self):
        return self.base_test(self.page.login_step(self.LOCKED_OUT_USER,self.PASSWORD), self.MSG_LOCKED_OUT_USER)

    #@pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_standard_user(self):
        return self.base_test(self.page.login_step(self.STANDARD_USER,TestData.PASSWORD), self.HOME_PAGE_URL)

    #@pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_problem_user(self):
        return self.base_test(self.page.login_step(self.PROBLEM_USER,TestData.PASSWORD), self.HOME_PAGE_URL)
    
    #@pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_performance_glitch_user(self):
        return self.base_test(self.page.login_step(self.PERFORMANCE_GLITCH_USER,TestData.PASSWORD), self.HOME_PAGE_URL)
    

if __name__ == '__main__':
    unittest.main()
