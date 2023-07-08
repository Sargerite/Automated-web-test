from Swag_Labs.pages.login_page_locators import Login_Page_Locators
from Swag_Labs.utils.config import Credencial
from selenium import webdriver
import unittest
driver = webdriver.Chrome()

class TestLogin(unittest.TestCase):

   def test_login_succesful(self):

       driver.get(Credencial.LOGIN_PAGE_URL)
       driver.find_element(*Login_Page_Locators.USERNAME_FIELD).send_keys(Credencial.locked_out_user_login)
       driver.find_element(*Login_Page_Locators.PASSWORD_FIELD).send_keys(Credencial.locked_out_user_passwd)
       driver.find_element(*Login_Page_Locators.LOGIN_BTN).click()


if __name__ == '__main__':
    unittest.main()
