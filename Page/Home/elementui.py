from Common.BaseUtil import BasePage


class Element(BasePage):
    url = 'https://element.eleme.cn/#/zh-CN/component/installation'

    def divider(self):
        self.by_xpath('//*[@id="app"]/div[2]/div/div[1]/div/div/div[1]/div[1]/div/div/ul/li[5]/div[6]/ul/li[9]/a')
