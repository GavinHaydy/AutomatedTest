import unittest
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
import os
from TestCase.test import TestBaidu
import time
now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
current_path = os.getcwd()  # 获取当前路径
case_path = os.path.join(current_path, 'TestCate')  # 用例路径 可以多个
report_path = os.path.join(current_path, 'Report')  # 结果报告存放路径


"""
    加载用例的方式一
    def run_all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test.py')
    return discover
"""
"""
    加载用例的方式二： 放在with open 上方
    testsuite = unittest.Testsuite()
    testsuite.addTest(unittest.TestLoader.loadTestFromTestCase(用例类名))
"""
"""
    加载方式三：
    testsuite = unittest.Testsuite()
    testsuite.addTest(类名('函数名'))
"""

if __name__ == '__main__':
    report_title = 'Example用例执行报告.html'
    result_path = os.path.join(report_path, report_title)

    # 报告描述
    desc = '用于展示修改样式后的HTMLTestRunner'
    testsuite = unittest.TestSuite()
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestBaidu))
    with open(result_path, 'w', encoding='utf-8') as report:
        runner = HTMLTestRunner(stream=report,
                                title=report_title,
                                description=desc)
        runner.run(testsuite)
