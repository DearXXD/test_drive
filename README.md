# test_drive
### 测试驱动
1. 在开发应用的每一个部分之前先编写和运行测试，然后再编写少量的代码让测试通过
2. 编写新代码，测试与预期结果是否一致
3. 重构修改旧代码时，使用测试保证修改的代码不会影响到应用的运行
---
#### 安装selenium 和 geckodriver
 1. 安装 selenium
      + pip install selenium
 2. 安装 geckodriver，下载 [geckodriver](https://github.com/mozilla/geckodriver/releases)，移动 geckodriver 到 /usr/local/bin/<br>
      + sudo mv ./geckodriver /usr/local/bin/<br>
      + sudo chmod a+x /usr/local/bin/geckodriver<br>
      
---
#### 测试驱动步骤
 1. 创建项目，完善配置文件
 2. 初始化本地仓库，链接并push远程仓库
 3. 写测试用例
 4. 根据测试完善功能

