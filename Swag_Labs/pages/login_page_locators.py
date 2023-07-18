from selenium.webdriver.common.by import By


class Login_Page_Locators():

    # locators
    LOGIN_PAGE_URL = "https://www.saucedemo.com/"
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    USERNAME = 'standard_user'
    PASSWD = 'secret_sauce'
