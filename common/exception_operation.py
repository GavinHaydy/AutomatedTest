"""
    @Author: TheRuffian
    @Email: bugpz2779@gmail.com
    @CSDN: 'https://blog.csdn.net/BUGPZ'
    @StackOverFlow: 'https://stackoverflow.com/users/12850648/theruffian'
"""
import os
import random
import traceback

SCREENSHOT_DIR = '/data/pythonObject/AutomatedTest'


def failure_monitor(self, img_path):
    test_case = self  # 将self赋值给test_case，以便下方的AssertionErrorPlus内部类可调用外部类的方法

    class AssertionErrorPlus(AssertionError):
        def __init__(self, msg):
            try:
                cur_method = test_case._testMethodName  # 当前test函数的名称
                unique_code = ''.join(random.sample('1234567890', 5))  # 随机生成一个值，以便区分同一个test函数内不同的截图
                file_name = '%s_%s.png' % (cur_method, unique_code)
                test_case.driver.get_screenshot_as_file(os.path.join(img_path, file_name))  # 截图生成png文件
                print('失败截图已保存到: %s' % file_name)
                msg += '\n失败截图文件: %s' % file_name
            except BaseException:
                print('截图失败: %s' % traceback.format_exc())

            super(AssertionErrorPlus, self).__init__(msg)

    return AssertionErrorPlus  # 返回AssertionErrorPlus类
