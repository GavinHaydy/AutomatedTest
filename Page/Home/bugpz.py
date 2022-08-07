from Common.BaseUtil import BasePage


class BugPZ(BasePage):
    url = 'https://bug-pz.cn/login'

    def username(self, search_key):
        self.by_xpath('//*[@id="app"]/div/div/div/div[2]/form/div[1]/div/div/div/input').send_keys(search_key)

    def password(self, search_key):
        self.by_xpath('//*[@id="app"]/div/div/div/div[2]/form/div[2]/div/div/div/input').send_keys(search_key)

    def login_btn(self):
        self.by_xpath('//*[@id="app"]/div/div/div/div[2]/form/div[3]/button').click()
