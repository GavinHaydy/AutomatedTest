import unittest
from time import sleep
from page.Home.baidu import BaiduPage
from common.base import open_browser

class TestBaidu(unittest.TestCase):

    def setUp(self):
        self.driver = open_browser('chrome')
        self.page = BaiduPage(self.driver)
        self.page.open_url(BaiduPage.url)

    def tearDown(self):
        self.driver.quit()

    def test_baidu_search_case(self):
        self.page.search_input("selenium ")
        self.page.search_button()
        sleep(2)
        self.assertEqual(self.page.get_title(), "selenium_百度搜索")
