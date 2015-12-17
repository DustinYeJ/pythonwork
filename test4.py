#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: yejun
@file: test4.py
@time: 15/12/10
"""

import time
import sys
from splinter import Browser

reload(sys)
sys.setdefaultencoding('utf-8')
browser = Browser('firefox')
# browser = Browser('firefox')

browser.visit('http://test.erp.iydsj.com:8088/erp_social1.0/login/userValidate')

username = '15158446952'
password = '123456'
browser.fill('loginForm.usernameInput', username)
browser.fill('loginForm.psdInput', password)
buttons = browser.find_by_xpath('//*[@id="login"]/div[4]/input[1]')
button = buttons.first
button.click()

browser.visit('http://test.erp.iydsj.com:8088/erp_social1.0/action/welcome/welcome/get')

html = browser.html

print html


#browser.fill('wd', 'dota')

# button = browser.find_by_name('tj_trnews')
# //button = browser.find_by_id('su')

# button.click()

# time.sleep(5)

# browser.quit()

