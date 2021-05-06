import unittest
from time import sleep
from selenium import webdriver
from Page.Home.baidu import BaiduPage
from Page.Home.elementui import Element
from Page.Home.bugpz import BugPZ
from DataProcessing import bugLOGIN
from ddt import ddt, data
from unittest import skip


@ddt
class TestBaidu(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.PhantomJS()     # 无界面浏览器  官网 phantomjs.org

    def test_baidu_search_case(self):
        page = BaiduPage(self.driver)
        page.open()
        page.search_input("selenium ")
        page.search_button()
        sleep(2)
        self.assertEqual(page.get_title(), "selenium_百度搜索")

    @skip
    def test_elem_case(self):
        page = Element(self.driver)
        page.open()
        page.divider()
        sleep(2)

    filepath = 'Config/bugpz-login.xlsx'
    dataS = bugLOGIN.ExcelUtil(filepath, 'Sheet1')
    datadict = dataS.dict_data()

    def login(self, username, password):
        page = BugPZ(self.driver)
        page.open()
        page.username(username)
        page.password(password)
        page.login_btn()

    @skip
    @data(*datadict)
    def test_login_case(self, test):
        self.login(test['username'], test['password'])

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
