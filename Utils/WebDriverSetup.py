import sys, os, inspect
sys.path.append(sys.path[0] + "/...")

import os
#Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())

from Locators.Locators import Locators
from TestData.TestData import TestData
from Pages.Pages import LoginPage

import warnings
import urllib3
from selenium import webdriver
import unittest
from time import sleep

# #Loop for choose FF or Chrome
# while True:
#     browser = input("Input 1 for FF and 2 for Chrome: ")
#     if (browser == "1") or (browser == "2"):
#         break

browser = 1

def set_enviroment_for_allure(self):
    file =  open("./allure-results/environment.properties", mode='w')
    file.write("Browser=" + self.driver.capabilities['browserName']+"\n")
    file.write("Browser.Version=" + self.driver.capabilities['browserVersion']+"\n")
    file.write("OS=" + self.driver.capabilities['platformName']+"\n")
    file.write("Stand=Production")
    file.close

class WebDriverSetup(unittest.TestCase):

    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        chrome_options=webdriver.ChromeOptions()
        self.browser = int(browser)
        #Run FF with 1 and run Chrome with 2
        if self.browser == 1:
            self.driver = webdriver.Firefox(executable_path = TestData.FIREFOX_EXECUTABLE_PATH)
        else:
            self.driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH, options=chrome_options)
        set_enviroment_for_allure(self)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        # To do the cleanup after test has executed.
        self.driver.close()
