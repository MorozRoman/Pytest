from selenium import webdriver
import time

class Fixture:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)

    def out(self):
        wd = self.wd
        wd.find_element_by_id("PH_logoutLink").click()

    def input_mail(self, accounts):
        self.site(mail_ru_="https://mail.ru/")
        wd = self.wd
        wd.find_element_by_id("mailbox__password").click()
        wd.find_element_by_id("mailbox__password").clear()
        wd.find_element_by_id("mailbox__password").send_keys(accounts.pas)
        wd.find_element_by_id("mailbox__login").click()
        wd.find_element_by_id("mailbox__login").clear()
        wd.find_element_by_id("mailbox__login").send_keys(accounts.name)
        self.input_button()
        time.sleep(3)

    def site(self,mail_ru_):
        wd = self.wd
        wd.get(mail_ru_)

    def input_button(self):
        wd = self.wd
        wd.find_element_by_id("mailbox__auth__button").click()

    def destroy(self):
        self.wd.close()