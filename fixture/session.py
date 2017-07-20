import time

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def input_mail(self, accounts):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("mailbox__password").click()
        wd.find_element_by_id("mailbox__password").clear()
        wd.find_element_by_id("mailbox__password").send_keys(accounts.pas)
        wd.find_element_by_id("mailbox__login").click()
        wd.find_element_by_id("mailbox__login").clear()
        wd.find_element_by_id("mailbox__login").send_keys(accounts.name)
        wd.find_element_by_class_name("mailbox__auth__remember__checkbox").click()
        self.input_button()
        # Нужно разобраться с ожиданием прогрузки страницы
        time.sleep(2)


    def input_button(self):
        wd = self.app.wd
        wd.find_element_by_id("mailbox__auth__button").click()

    def out_mail(self):
        wd = self.app.wd
        wd.find_element_by_id("PH_logoutLink").click()
