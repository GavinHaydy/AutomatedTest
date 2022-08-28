import unittest
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
import os
from testcase.test_web import TestBaidu
import time
import smtplib  # 邮件库
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


now = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
report_time = time.strftime('%Y-%m-%d-%H.%M.%S', time.localtime(time.time()))
current_path = os.getcwd()  # 获取当前路径
case_path = os.path.join(current_path, 'TestCate')  # 用例路径 可以多个
report_path = os.path.join(current_path, 'Report')  # 结果报告存放路径


"""
    加载用例的方式一
    def run_all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_web.py')
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


def email_setting():
    file = os.path.join(report_path, report_title)  # 获取测试用例报告
    sendfile = open(file, 'rb').read()
    att = MIMEText(sendfile, 'base64', 'utf-8')
    print(sendfile, '文件名', file)
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename= ' + str(report_time) + 'TestReport.html'    # 附件名称 别用中文
    print(att['Content-Disposition'])
    print(report_title)
    msg = MIMEMultipart()
    msg['Subject'] = '自动化测试报告'  # '主题'
    msg.attach(MIMEText('这里是邮件的正文'))    # 正文
    msg.attach(att)  # 附件
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com', 25)  # 邮箱服务器及端口
    smtp.login('email', 'password')    # 发送的账号密码
    smtp.sendmail('13558622779@163.com', 'bugpz2779@gmail.com', msg.as_string())     # 参数 1: 发送的邮箱， 2 接收的邮箱
    smtp.quit()


if __name__ == '__main__':
    report_title = (str(now) + '用例执行报告.html')
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

    email_setting()
