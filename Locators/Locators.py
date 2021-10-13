from selenium.webdriver.common.by import By

class Locators():
    # --- Login Page Locators ---
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")