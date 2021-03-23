# AutomatedTest
    简单的PO模式UI自动化测试脚本模板
    ddt模式后续会慢慢完善

##使用说明:
    需要的三方库在requirements.txt,安装方法如下:
    pip install -r requirements.txt


目录结构说明
```
Business 
    放置封装文件，目前封装了查找元素的几种方法
Page
    页面的查找元素文件
Report
    用于存放用例执行报告，在run.py中可自行修改
TestCase
    完整的用例执行逻辑脚本
run.py
    用例执行入口
```