
class TestData():
    CHROME_EXECUTABLE_PATH = "./Drivers/chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = "./Drivers/geckodriver.exe"

    BASE_URL = "https://www.saucedemo.com/"
    HOME_PAGE_URL = "https://www.saucedemo.com/inventory.html"

    MSG_USER_BLANK = "Epic sadface: Username is required"
    MSG_PASS_BLANK = "Epic sadface: Password is required"
    MSG_WRONG_ACC = "Epic sadface: Username and password do not match any user in this service"
    MSG_LOCKED_OUT_USER = "Epic sadface: Sorry, this user has been locked out."

    STANDARD_USER = "standard_user"
    LOCKED_OUT_USER = "locked_out_user"
    PROBLEM_USER ="problem_user"
    PERFORMANCE_GLITCH_USER = "performance_glitch_user"
    PASSWORD = "secret_sauce"
    NULL = ""
