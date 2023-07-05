from Swag_Labs.pages.login_page_locators import Locators
from Swag_Labs.utils.config import Credencial
from selenium import webdriver
import unittest
driver = webdriver.Chrome()

class TestLogin(unittest.TestCase):

    def test_login_succesful(self):

        driver.get(Credencial.LOGIN_PAGE_URL)
        driver.find_element(*Locators.USERNAME_FIELD).send_keys(Credencial.standard_user_login)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credencial.standard_user_passwd)
        driver.find_element(*Locators.LOGIN_BTN).click()


if __name__ == '__main__':
    unittest.main()


