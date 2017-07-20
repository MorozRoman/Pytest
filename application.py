import webium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webium import BasePage, Find
from selenium.webdriver.remote.webelement import WebElement
from webium.wait import wait

# Webium
class Elements(WebElement):
    search_button = Find(by=By.CLASS_NAME, value='mos-layout-icon-search_black')
    text_input = Find(by=By.CLASS_NAME, value='tt-input')

class MainPage(BasePage):
    search = Find(Elements, by=By.CLASS_NAME, value='mos-search-form')

    def __init__(self):
        super(MainPage, self).__init__(url='http://www.mos.ru')

    def button(self):
        self.search.search_button.click()

class SearchResultPage(BasePage):
    widget = Find(by=By.CLASS_NAME, value="wdg-mayor")

class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        webium.driver._driver_instance = self.driver
        driver = self.driver
        driver.maximize_window()

    def open_site(self):
        page = MainPage()
        page.open()
        return page

    def search_by_name(self):
        page = self.open_site()
        page.button()
        page.search.text_input.send_keys(u"Собянин")
        page.button()
        return SearchResultPage

    def element_present(self):
        result_page = SearchResultPage()
        wait(lambda: result_page.is_element_present('widget'), timeout_seconds=2)


    def destroy(self):
        self.driver.close()




