import time

import sys

sys.path.append(sys.path[0] + "/...")

import os
#Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())

from TestData.TestData import TestData
from Objects.Object import HomeObject

class LoginPage(HomeObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def login_step(self, username, password):
        self.username(username)
        self.password(password)
        self.login_button()
        time.sleep(1)

    def login_fail(self, username, password):
        self.login_step(username, password)
        return self.error_msg()

    def login_success(self, username, password):
        self.login_step(username, password)
        return self.homepage()
