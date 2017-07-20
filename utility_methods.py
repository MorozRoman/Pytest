import webium
from selenium import webdriver
from selenium.webdriver.common.by import By
from waiting import wait
from webium import BasePage, Finds
import time


class MainPage(BasePage):
    services = Finds(by=By.CLASS_NAME, value='popular-item')

    def __init__(self):
        super(MainPage, self).__init__(url='http://www.mos.ru')

class Utility:
    def __init__(self):
        self.driver = webdriver.Chrome()
        webium.driver._driver_instance = self.driver
        driver = self.driver
        driver.maximize_window()

    def open_site(self):
        page = MainPage()
        page.open()
        return page

    def elements_present(self):
        page = self.open_site()
        time.sleep(2)
        page.services == "10"
        # wait(lambda: page.services == "10", timeout_seconds=5)


    def destroy(self):
        self.driver.close()

