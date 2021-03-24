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

Jenkins 部署 以windows举例
```
    1.进入官网下载jenkins.war
    2.切换到下载目录并执行 java -jar jenkins.war --httpPort=XXXX  XXXX：自己指定端口号
    3.启动好后使用浏览器访问localhost:XXXX  按照页面提示找到本地密码输入， 然后创建账号
构建配置：
    1.新建任务 输入任务名并选择 “构建一个自由风格的软件项目” （Freestyle project） 然后保存
    2.选择"丢弃旧版本" (Discard old builds)
    3.源码管理按照自己的实际情况选择，我例子没用git，所以选择无
    4.构建触发器根据实际情况选择，如果想手动执行可以不选，如果想定时就选择“定期建立”（Build periodically）
定时语法参考： https://blog.csdn.net/u013250071/article/details/81000777
    5.构建环境根据实际情况自己决定
    6.增加构建步骤：选择“执行windows批处理命令”（Execute Windows batch command），在文本域里输入命令
举个栗子：
    我的执行文件目录run.py在G:\data\wwwroot\AutomatedTest  那么命令为：
    G:
    cd data/wwwroot/AutomatedTest
    python run.py
    7.建立后操作自行选择，点击保存    
    8.保存后会返回你新建的任务页，点击左边操作界面的“构建”（Build Now）就开始执行任务了
```