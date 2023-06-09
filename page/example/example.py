from common.base import BasePage


class ExamplePage(BasePage):

    # 定位搜索框输入搜索数据
    SEARCH_INPUT = ('id', "kw")

    # 点击百度一下按钮搜索
    SEARCH_BUTTON = ('id', "su")


class ExamplePage2(BasePage):
    WECHAT_ENV = ("css selector", "#m-product > ul > li.q-icons.prod-2 > a:nth-child(2)")
