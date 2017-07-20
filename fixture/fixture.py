from selenium import webdriver
from fixture.session import SessionHelper

class Fixture:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(20)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://mail.ru/")


    def input_button(self):
        wd = self.wd
        wd.find_element_by_id("mailbox__auth__button").click()


    def destroy(self):
        self.wd.close()