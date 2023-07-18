from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class BasePage():

    def init(self, driver):
        self.driver = webdriver.Chrome()

    def wait_for_element(self, locator, timeout=10):
        """Waits for an element to be visible on the page before performing actions."""
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        """Clicks on the specified element."""
        element = self.wait_for_element(locator)

    def enter_text(self, locator, text):
        """Enters text into the specified text input element."""
        element = self.wait_for_element(locator)
        # element.clear()
        element.send_keys(text)

    def get_element_text(self, locator):
        """Returns the text of the specified element."""

    def get_page_title(self):
        """Returns the title of the current page."""

    def wait_for_url_to_load(self, driver, timeout, url):
        wait = WebDriverWait(driver, timeout)
        wait.until(EC.url_to_be(url))