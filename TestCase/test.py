import unittest
from time import sleep
from selenium import webdriver
from Page.Home.baidu import BaiduPage
from Page.Home.elementui import Element


class TestBaidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_baidu_search_case(self):
        page = BaiduPage(self.driver)
        page.open()
        page.search_input("selenium ")
        page.search_button()
        sleep(2)
        self.assertEqual(page.get_title(), "selenium_百度搜索")

    def test_elem_case(self):
        page = Element(self.driver)
        page.open()
        page.divider()
        sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
