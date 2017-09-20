# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class TodoTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_list_in_ul(self, row_text):
        html_list = self.browser.find_element_by_id("myId")
        items = html_list.find_elements_by_tag_name("li")
        l = []
        for item in items:
            text = item.text
            l.append(text)
        self.assertIn(row_text, l)

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn(u"待办事项", self.browser.title)

        body_title = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(u"待办事项", body_title)

        body_welcome = self.browser.find_element_by_tag_name('h3').text
        self.assertIn(u"welcome", body_welcome)

        inputbox = self.browser.find_element_by_name('event_name')
        inputbox.send_keys(u"购买《Python核心编程》")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_list_in_ul(u"购买《Python核心编程》")

        inputbox = self.browser.find_element_by_name('event_name')
        inputbox.send_keys(u"购买《测试驱动开发》")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_list_in_ul(u"购买《测试驱动开发》")
        self.check_list_in_ul(u"购买《Python核心编程》")
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()