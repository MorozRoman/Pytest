import pytest
from utility_methods import Utility


@pytest.fixture
def app(request):
    fixture = Utility()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_present(app):
    app.elements_present()






# UnitTest
# class one_mos(unittest.TestCase):
# 
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#     def test_popular(self):
#         driver = self.driver
#         driver.get("http://www.mos.ru")
#         self.assertEqual(len(driver.find_elements_by_class_name('catalog-services-popular__item')), 10)
#         time.sleep(5)
#     def tearDown(self):
#         self.driver.close()
# if __name__ == "__main__":
#     unittest.main()
