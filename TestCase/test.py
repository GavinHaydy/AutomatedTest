import unittest
from time import sleep
from selenium import webdriver
from Page.Home.baidu import BaiduPage
from Common.BaseUtil import open_browser


class TestBaidu(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = open_browser('chrome')     # 无界面浏览器  官网 phantomjs.org
        self.driver.get(BaiduPage.url)
        self.page = BaiduPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_baidu_search_case(self):
        self.page.search_input("selenium ")
        self.page.search_button()
        sleep(2)
        self.assertEqual(self.page.get_title(), "selenium_百度搜索")


if __name__ == '__main__':
    unittest.main()
