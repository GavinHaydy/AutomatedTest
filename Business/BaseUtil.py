from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):
    """
       基础Page层，封装一些常用方法
    """

    def __init__(self, driver):
        self.driver = driver

    def open(self, url=None):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    def by_id(self, id):
        return self.driver.find_element_by_id(id)

    def by_name(self, name):
        return self.driver.find_element_by_name(name)

    def by_class_name(self, class_name):
        return self.driver.find_element_by_class_name(class_name)

    def by_tag_name(self, tag_name):
        return self.driver.find_element_by_tag_name(tag_name)

    def by_link_text(self, link_text):
        return self.driver.find_element_by_link_text(link_text)

    def by_partial_link_text(self, partial_link_text):
        return self.driver.find_element_by_partial_link_text(partial_link_text)

    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def by_css(self, css):
        return self.driver.find_element_by_css_selector(css)

    def get_title(self):
        return self.driver.title

    def get_text(self, xpath):
        return self.by_xpath(xpath).text

    def size(self, wide, high): # 设置浏览器大小
        return self.driver.set_window_size(wide, high)

    '''鼠标事件相关封装'''
    def right_click(self, path):    # 鼠标右击
        return ActionChains(self.driver).context_click(path).perform()

    def double_click(self, path):   # 双击
        return ActionChains(self.driver).double_click(path).perform()

    def drag_and_drop(self, start_path, end_path):    # 鼠标拖放（start_path=鼠标拖动源元素， end_path=鼠标释放目标元素）
        return ActionChains(self.driver).drag_and_drop(start_path, end_path).perform()

    def move_to_element(self, path):    # 鼠标悬停
        return ActionChains(self.driver).move_to_element(path).perform()
