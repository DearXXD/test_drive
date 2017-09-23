# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class TodoTest(unittest.TestCase):

    # 测试函数执行前执行
    def setUp(self):
        '''
        启动浏览器
        '''
        self.browser = webdriver.Firefox()

    # 测试函数执行后执行
    def tearDown(self):
        '''
        关闭浏览器
        '''
        self.browser.quit()

    def check_list_in_ul(self, check_text):
        '''
        检查check_text的值是否在li中
        :param check_text:被检查的值
        :return:是否在li中
        '''
        html_list = self.browser.find_element_by_id("myId")
        items = html_list.find_elements_by_tag_name("li")
        l = []
        for item in items:
            text = item.text
            l.append(text)
        self.assertIn(check_text, l)

    def test_todo(self):
        '''
        1.小明打开浏览器，输入地址：http://localhost/，打开了一个页面
        2.小明看见页面的标题和头部都包含“待办事项”这个词
        3.页面包含一句欢迎语，邀请小明输入一个待办事项并点击提交按钮
        4.小明在输入框中输入了“购买《Python核心编程》”，并点击提交按钮
        5.页面中显示了“1. 购买《Python核心编程》”
        6.小明在输入框中输入了“购买《测试驱动开发》”，并点击提交按钮
        7.页面中显示了两个待办事项
        '''
        self.browser.get('http://localhost/')
        self.assertIn(u"待办事项", self.browser.title)

        body_title = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(u"待办事项", body_title)

        body_welcome = self.browser.find_element_by_tag_name('h3').tex
        self.assertIn(u"welcome", body_welcome)

        inputbox = self.browser.find_element_by_name('event_name')
        inputbox.send_keys(u"购买《Python核心编程》")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)   # time for page refresh

        self.check_list_in_ul(u"1. 购买《Python核心编程》")

        inputbox = self.browser.find_element_by_name('event_name')
        inputbox.send_keys(u"购买《测试驱动开发》")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_list_in_ul(u"2. 购买《测试驱动开发》")
        self.check_list_in_ul(u"1. 购买《Python核心编程》")
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()