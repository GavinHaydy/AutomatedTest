import unittest

from common.document_operation import get_yaml
from common.base import open_browser
from page.example.example import ExamplePage2


class TestBaidu(unittest.TestCase):

    def setUp(self):
        self.driver = open_browser('chrome')
        self.dri = ExamplePage2(self.driver)
        self.dri.open_url(get_yaml('../config/env.yaml', 'url23'))

    def tearDown(self):
        self.driver.quit()

    def test_example_qq_num(self):
        a = self.dri.locate_with_left(self.dri.WECHAT_ENV, 'tag name', 'a')
        print(self.dri.find_element(a).text)
