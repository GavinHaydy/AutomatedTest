import unittest
from time import sleep

from common.document_operation import get_yaml
from page.example.example import ExamplePage
from common.base import open_browser, BasePage


class TestBaidu(unittest.TestCase):

    def setUp(self):
        self.driver = open_browser('chrome', logs=True)
        self.page = ExamplePage(self.driver)
        self.page.open_url(get_yaml('../config/env.yaml', 'url_baidu'))

    def tearDown(self):
        self.driver.quit()

    def test_baidu_search_case(self):
        self.page.send_keys(self.page.SEARCH_INPUT, 'selenium')
        self.page.click(self.page.SEARCH_BUTTON)
        sleep(2)
        for typelog in self.driver.log_types:
            perfs = self.driver.get_log(typelog)
            print(perfs)
            for row in perfs:
                print(row)
        self.assertEqual(self.page.get_title(), "selenium_百度搜索")
