from selenium.webdriver.common.by import By

class Inventory_page_locators():

    INVENTORY_PAGE_URL = 'https://www.saucedemo.com/inventory.html'
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    BURGER_ALL_ITEMS = (By.ID, 'inventory_sidebar_link')
    BURGER_ABOUT = (By.ID, 'about_sidebar_link')
    BURGER_LOGOUT = (By.ID, 'logout_sidebar_link')
    BURGER_RESET_APP_STATE = (By.ID, 'reset_sidebar_link')