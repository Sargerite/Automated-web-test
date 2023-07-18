import Swag_Labs.pages.base_page
from Swag_Labs.pages.login_page_locators import Login_Page_Locators
from selenium.webdriver.support import expected_conditions as EC
from Swag_Labs.pages.base_page import *
from Swag_Labs.utils.config import Credential
from selenium import webdriver
import unittest
driver = webdriver.Chrome()


class TestLogin(unittest.TestCase):

    def test_login_successful(self):

        driver.get(Credential.LOGIN_PAGE_URL)
        driver.find_element(*Login_Page_Locators.USERNAME_FIELD).send_keys(Credential.STANDARD_USER_LOGIN)
        driver.find_element(*Login_Page_Locators.PASSWORD_FIELD).send_keys(Credential.standard_user_passwd)
        driver.find_element(*Login_Page_Locators.LOGIN_BTN).click()
        Swag_Labs.pages.base_page.WebDriverWait(driver,
                                                10,
                                                Credential.INVENTORY_PAGE_URL)
        self.assertEquals(driver.current_url,
                          Credential.INVENTORY_PAGE_URL,
                          "URL mismatch. Expected inventory page URL")


if __name__ == '__main__':
    unittest.main()
