from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.relative_locator import locate_with, with_tag_name, RelativeBy


def open_browser(browser: str = 'chrome', **kwargs):
    """

    Args:
        browser: 浏览器名称
        **kwargs: 浏览器参数

    Returns: 浏览器对象

    """
    if browser.lower() == "firefox":
        driver = webdriver.Firefox(**kwargs)
    elif browser.lower() == "chrome":
        if kwargs and kwargs.get('logs'):
            caps = DesiredCapabilities.CHROME
            caps['loggingPrefs'] = {
                'browser': 'ALL',
                'performance': 'ALL'
            }
            caps['perfLoggingPrefs'] = {
                'enableNetwork': True,
                'enablePage': False,
                'enableTimeline': False
            }
            option = webdriver.ChromeOptions()
            option.add_argument('--no-sandbox')
            option.add_experimental_option('w3c', True)
            driver = webdriver.Chrome(desired_capabilities=caps, options=option)
        else:
            driver = webdriver.Chrome(**kwargs)
    elif browser.lower() == "ie":
        driver = webdriver.Ie(**kwargs)
    elif browser.lower() == "edge":
        driver = webdriver.Edge(**kwargs)
    elif browser.lower() == "safari":
        driver = webdriver.Safari(**kwargs)
    else:
        raise Exception("未知的浏览器或未封装的浏览器")
    return driver


class BasePage(object):
    """
       基础Page层，封装一些常用方法
    """

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url: str):  # 打开url
        """

        Args:
            url:    the url you want to open

        Returns:

        """
        try:
            if url.startswith("http://") or url.startswith("https://"):
                self.driver.get(url)
                self.driver.maximize_window()
            else:
                self.driver.get("http://" + url)
                self.driver.maximize_window()
        except Exception as e:
            raise e

    def find_element(self, loc, timeout=10):  # 定位元素
        #   根据loc类型处理
        if isinstance(loc, RelativeBy):
            return self.driver.find_element(loc)
        else:
            return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(loc))

    def find_elements(self, loc, timeout=10):  # 定位一组元素
        if isinstance(loc, RelativeBy):
            return self.driver.find_elements(loc)
        else:
            return WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(loc))

    def click(self, loc):  # 点击元素
        return self.find_element(loc).click()

    def send_keys(self, loc, text=None):  # 发送文本
        return self.find_element(loc).send_keys(text)

    def get_title(self):
        return self.driver.title

    def get_text(self, loc):
        """

        Args:
            loc:

        Returns: the text of tag

        """
        return self.find_element(loc).text

    def size(self, wide, high):  # 设置浏览器大小
        return self.driver.set_window_size(wide, high)

    def maxsize(self):
        return self.driver.set_window_size()

    def minsize(self):
        return self.driver.minimize_window()

    def tag_value(self, loc, attname: str = 'outerHTML'):
        return self.find_element(loc).getAttribute(attname)

    """相对定位 Relative positioning"""

    @staticmethod
    def tag_name_with(tag_name: str):
        return with_tag_name(tag_name)

    def locate_with_above(self, el, *loc):
        return locate_with(*loc).above(self.find_element(el))

    def locate_with_below(self, el, *loc):
        return locate_with(*loc).below(self.find_element(el))

    # @staticmethod
    def locate_with_left(self, el, *loc):
        # print(*loc)
        return locate_with(*loc).to_left_of(self.find_element(el))

    # @staticmethod
    def locate_with_right(self, el, *loc):
        return locate_with(*loc).to_right_of(self.find_element(el))

    def locate_with_near(self, el, *loc):
        return locate_with(*loc).near(self.find_element(el))

    def close(self):
        return self.driver.close()

    def quit(self):
        return self.driver.quit()

    '''鼠标事件相关封装'''

    def right_click(self, ele):  # 鼠标右击
        return ActionChains(self.driver).context_click(ele).perform()

    def double_click(self, ele):  # 双击
        return ActionChains(self.driver).double_click(ele).perform()

    def drag_and_drop(self, start_ele, end_ele):  # 鼠标拖放（start_path=鼠标拖动源元素， end_path=鼠标释放目标元素）
        return ActionChains(self.driver).drag_and_drop(start_ele, end_ele).perform()

    def move_to_element(self, ele):  # 鼠标悬停
        return ActionChains(self.driver).move_to_element(ele).perform()

    '''其他操作封装'''

    def get_picture(self, file_save_path):  # 截图并保存在指定位置
        return self.driver.get_screenshot_as_file(file_save_path)

    def execute_js(self, js_code: str, *args, is_async='n'):
        """
        Executes JavaScript in the current window/frame.

        Args:
            js_code:  code of JavaScript
            *args:
            is_async: y|n  Asynchronously executed or not

        Returns:

        """
        if is_async.lower() == 'n':
            return self.driver.execute_script(js_code, *args)
        elif is_async.lower() == 'y':
            return self.driver.execute_async_script(js_code, *args)

    def get_url(self):  # 获取当前url
        return self.driver.current_url()

    def get_source(self):  # 获取当前页源
        return self.driver.page_source()

    def max_window(self):  # 最大化浏览器
        return self.driver.maximize_window()

    def get_handle(self):
        return self.driver.current_window_handle()

    def get_handles(self):
        return self.driver.window_handle()
