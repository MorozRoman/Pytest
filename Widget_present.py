import pytest
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_search(app):
    app.search_by_name()
    app.element_present()





# Unittest
# class two_mos(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#     def test_serach(self):
#         driver = self.driver
#         driver.maximize_window()
#         driver.get("http://www.mos.ru")
#         driver.find_element_by_class_name('mos-layout-icon-search_black').click()
#         driver.find_element_by_class_name('tt-input').send_keys(u'Собянин')
#         driver.find_element_by_class_name('mos-layout-icon-search_black').click()
#         driver.implicitly_wait(10)
#         driver.find_element_by_class_name('wdg-mayor')
#         # time.sleep(5)
#     def tearDown(self):
#         self.driver.close()
# if __name__ == "__main__":
#     unittest.main()
