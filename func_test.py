# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/usr/bin/firefox')
browser = webdriver.Firefox(firefox_binary=binary)

# browser = webdriver.Firefox()
browser.get("http://127.0.0.1:8000")


assert u"待办事项" in browser.title
assert u"待办事项" in browser.find_element_by_tag_name('h1').text
assert u"welcome" in browser.find_element_by_tag_name('h3').text
assert u"Save" in browser.find_element_by_name('submit').text
# browser.find_element_by_name('event_name').send_keys(u'购买《Python核心编程》')
# browser.find_element_by_name('event_name').send_keys(Keys.ENTER)



html_list =browser.find_element_by_id("myId")
items = html_list.find_elements_by_tag_name("li")
l = []
for item in items:
    text = item.text
    l.append(text)



assert u"购买《Python核心编程》" in l
assert u"购买《测试驱动开发》" in l
