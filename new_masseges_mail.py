# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

# def is_alert_present(wd):
#     try:
#         wd.switch_to_alert().text
#         return True
#     except:
#         return False

class new_masseges_mail(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_new_masseges_mail(self):
        success = True
        wd = self.wd
        wd.get("https://yandex.ru/")
        wd.find_element_by_link_text("Погода").click()
        wd.find_element_by_id("header2input").click()
        # wd.find_element_by_id("header2input").clear()
        wd.find_element_by_id("header2input").send_keys("Кимры")
        wd.find_element_by_xpath("//div[@class='header2__left']//button[.='Найти']").click()
        wd.find_element_by_link_text("Кимры").click()
        wd.find_element_by_xpath("//div[@class='header__left']/a/img").click()
        wd.find_element_by_css_selector("img.image").click()
        wd.find_element_by_id("text").click()
        wd.find_element_by_id("text").send_keys("\\9")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
