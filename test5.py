#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: yejun
@file: test5.py
@time: 15/12/14
"""

from splinter import Browser
import sys

browser = Browser('firefox')

browser.visit('http://www.baidu.com')
browser.fill('wd', 'python')

button = browser.find_by_id('su')

button.click()

button = browser.find_by_xpath('//*[@id="s_tab"]/a[5]')

button.click()
