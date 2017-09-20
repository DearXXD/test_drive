# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

'''
        1.小明打开浏览器，输入地址：http://localhost/，打开了一个页面
        2.小明看见页面的标题和头部都包含“待办事项”这个词
        3.页面包含一句欢迎语，邀请小明输入一个待办事项并点击提交按钮
        4.小明在输入框中输入了“购买《Python核心编程》”，并点击提交按钮
        5.页面中显示了“1. 购买《Python核心编程》”
        6.小明在输入框中输入了“购买《测试驱动开发》”，并点击提交按钮
        7.页面中显示了两个待办事项
'''

binary = FirefoxBinary('/usr/bin/firefox') # find the oath of firefox
browser = webdriver.Firefox(firefox_binary=binary)

#1
browser.get("http://localhost:8000")

def check_list_in_ul(check_text):
    '''
    检查check_text的值是否在li中
    :param check_text:被检查的值
    :return:是否在li中
    '''
    html_list = browser.find_element_by_id("myId")
    items = html_list.find_elements_by_tag_name("li")
    l = []
    for item in items:
        text = item.text
        l.append(text)
    assert check_text in l

# 2
assert u"待办事项" in browser.title
assert u"待办事项" in browser.find_element_by_tag_name('h1').text

# 3
assert u"welcome" in browser.find_element_by_tag_name('h3').text
assert u"Save" in browser.find_element_by_name('submit').text

# 4
browser.find_element_by_name('event_name').send_keys(u'购买《Python核心编程》')
browser.find_element_by_name('event_name').send_keys(Keys.ENTER)
time.sleep(1)

# 5
check_list_in_ul(u"购买《Python核心编程》")

# 6
browser.find_element_by_name('event_name').send_keys(u'购买《测试驱动开发》')
browser.find_element_by_name('event_name').send_keys(Keys.ENTER)
time.sleep(1)

# 7
check_list_in_ul(u"购买《Python核心编程》")
check_list_in_ul( u"购买《测试驱动开发》")

browser.quit()

