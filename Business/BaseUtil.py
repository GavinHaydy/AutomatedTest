from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def open_browser(browser: str='chrome', **kwargs):
    """

    Args:
        browser: 浏览器名称
        **kwargs: 浏览器参数

    Returns: 浏览器对象

    """
    if browser.lower() == "firefox":
        driver = webdriver.Firefox(**kwargs)
    elif browser.lower() == "chrome":
        driver = webdriver.Chrome(**kwargs)
    elif browser.lower() == "ie":
        driver = webdriver.Ie(**kwargs)
    elif browser.lower() == "edge":
        driver = webdriver.Edge(**kwargs)
    elif browser.lower() == "phantomjs":
        driver = webdriver.PhantomJS(**kwargs)
    else:
        raise Exception("Unsupported browser")
    return driver


class BasePage(object):
    """
       基础Page层，封装一些常用方法
    """

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url:str):  # 打开url
        """

        Args:
            url:    the url you want to open

        Returns:

        """
        try:
            if url.startswith("http://") or url.startswith("https://"):
                self.driver.get(url)
                self.driver.maximizi_window()
            else:
                self.driver.get("http://" + url)
                self.driver.maximizi_window()
                self.driver.maximizi_window()
        except Exception as e:
            raise e



    def find_element(self, loc, timeout=10):  # 定位元素
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(loc))

    def find_elements(self, loc, timeout=10):  # 定位一组元素
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(loc))

    def click(self, loc):  # 点击元素
        return self.find_element(loc).click()

    def send_keys_(self, loc, text=None):  # 发送文本
        return self.find_element(loc).send_keys(text)

    def get_title(self):
        return self.driver.title

    def get_text(self, loc):
        return self.find_element(loc).text

    def size(self, wide, high):  # 设置浏览器大小
        return self.driver.set_window_size(wide, high)

    '''鼠标事件相关封装'''

    def right_click(self, path):  # 鼠标右击
        return ActionChains(self.driver).context_click(path).perform()

    def double_click(self, path):  # 双击
        return ActionChains(self.driver).double_click(path).perform()

    def drag_and_drop(self, start_path, end_path):  # 鼠标拖放（start_path=鼠标拖动源元素， end_path=鼠标释放目标元素）
        return ActionChains(self.driver).drag_and_drop(start_path, end_path).perform()

    def move_to_element(self, path):  # 鼠标悬停
        return ActionChains(self.driver).move_to_element(path).perform()

    '''其他操作封装'''

    def get_picture(self, file_save_path):  # 截图并保存在指定位置
        return self.driver.get_screenshot_as_file(file_save_path)

    def use_js(self, js_code):  # 运行js代码
        return self.driver.execute_script(js_code)

    def get_url(self):  # 获取当前url
        return self.driver.current_url()

    def get_source(self):  # 获取当前页源
        return self.driver.page_source()

    def max_window(self):  # 最大化浏览器
        return self.driver.maximizi_window()

