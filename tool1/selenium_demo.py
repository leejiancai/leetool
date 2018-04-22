#!/bin/usr/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Author: lijiancai
# File Name: selenium_demo.py
# Contact: 958000432@qq.com
# Created Time: 2018/4/22 下午12:19
# Version: 1.0
# Description:
#
# Change Activities:
#           2018/4/22:
# ======================================================================================================================

from selenium import webdriver

browser = webdriver.Firefox()


try:
    print("before try")
    browser.get('http://www.baidu.com')
    print("after try")

    # 获取一个元素
    elem = browser.find_element_by_link_text('新闻')

    # 点击此元素
    elem.click()

    # 浏览器后退
    browser.back()

    # 查找输入框
    elem = browser.find_element_by_css_selector('input[name="wd"]')

    elem.send_keys('123')

    elem.submit()


except Exception as e:
    print(e)

