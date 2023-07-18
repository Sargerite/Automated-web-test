import unittest

from selenium import webdriver

from Swag_Labs.pages.login_page_locators import Login_Page_Locators
from Swag_Labs.utils.config import Credential

driver = webdriver.Chrome()


class TestLogin(unittest.TestCase):

   def test_login_successful(self):

       driver.get(Credential.LOGIN_PAGE_URL)
       driver.find_element(*Login_Page_Locators.USERNAME_FIELD).send_keys(Credential.locked_out_user_login)
       driver.find_element(*Login_Page_Locators.PASSWORD_FIELD).send_keys(Credential.locked_out_user_passwd)
       driver.find_element(*Login_Page_Locators.LOGIN_BTN).click()
       self.assertEquals(driver.find_element(*Login_Page_Locators.ERROR_MSG),
                         driver.find_element(*Login_Page_Locators.ERROR_MSG),
                         "Login error info missing")


if __name__ == '__main__':
    unittest.main()
