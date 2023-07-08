from selenium.webdriver.common.by import By


class Login_Page_Locators():

    # locators
    LOGIN_PAGE_URL = "https://www.saucedemo.com/"
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    USERNAME = 'standard_user'
    PASSWD = 'secret_sauce'
