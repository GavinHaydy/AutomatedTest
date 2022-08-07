from Common.BaseUtil import BasePage


class BaiduPage(BasePage):
    url = 'www.baidu.com'

    # 定位搜索框输入搜索数据
    def search_input(self, text=None):
        self.send_keys(['id', "kw"], text)

    # 点击百度一下按钮搜索
    def search_button(self):
        self.click(('id', "su"))

    def title(self):
        return self.get_title()
