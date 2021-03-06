import sys
import os
import pytest
sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())

from unittest import TestLoader, TestSuite, TextTestRunner
from TestCases.Test_Login import Test_Login_Page


if __name__ == "__main__":

    #os.system("C:/Users/USER/scoop/apps/allure/2.14.0/bin/allure generate --clean --output " + './Reports')
    pytest.main(['-p', 'no:warnings', '-sq', '-n 2','--alluredir','./allure-results','./TestCases/Test_Login.py'])
    #pytest.main(['-s', '-q','./TestCases/Test_Login.py'])
    #Open allue report via browser
    #os.system("C:/Users/USER/scoop/apps/allure/2.14.0/bin/allure serve " + './Reports')
