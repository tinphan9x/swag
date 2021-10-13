import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import sys, os, inspect
sys.path.append(sys.path[0] + "/...")

import os
#Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())

from Locators.Locators import Locators
from TestData.TestData import TestData

class HomeObject():
    """This class is the parent class for all the pages in our application."""
    """It contains all common elements and functionalities available to all pages."""

    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver = driver

    def username(self, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.USERNAME)).send_keys(text)

    def password(self, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.PASSWORD)).send_keys(text)

    def login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON)).click()

    def error_msg(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.ERROR_MSG)).text

    def homepage(self):
        return self.driver.current_url
