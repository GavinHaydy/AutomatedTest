from Business.BaseUtil import BasePage


class BaiduPage(BasePage):
    url = "http://www.baidu.com"

    # 定位搜索框输入搜索数据
    def search_input(self, search_key):
        self.by_id("kw").send_keys(search_key)

    # 点击百度一下按钮搜索
    def search_button(self):
        self.by_id("su").click()
