#! python3
# -*- coding:utf-8 -*-

from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com')
browser.find_element_by_link_text('登录').click()
browser.find_element_by_css_selector("span.name.signup-social-buttons.js-toggle-sns-buttons").click()
browser.find_element_by_class_name("js-bindqq").click()
cur_handle = browser.current_window_handle
all_handles = browser.window_handles        # 获取所有窗口句柄
for handle in all_handles:
	if handle != cur_handle:
		browser.switch_to.window(handle)
		browser.switch_to.frame('ptlogin_iframe')       # 需先跳转到frame框架!!
		browser.find_element_by_id('switcher_plogin').click()
		browser.find_element_by_id('u').send_keys('*********')
		browser.find_element_by_id('p').send_keys('*********')
		browser.find_element_by_id('login_button').click()
browser.switch_to.window(cur_handle)