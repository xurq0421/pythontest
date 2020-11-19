#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/29 16:42
# @Author : xurq
# @Site : 
# @File : seleniumtest.py
# @Software: PyCharm

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('E:\核心自动化\\test\\test1.html')

# 父节点定位子节点
# 串联寻找
table_text1 = driver.find_element_by_id('B').find_element_by_tag_name('div').text
# print(table_text1)

# xpath父子关系查找
table_text2 = driver.find_element_by_xpath("//div[@id='B']/div/div").text
print(table_text2)

# css selector父子关系查找
table_text3 = driver.find_element_by_css_selector("div#B>div").text
# print(table_text3)

# css selector nth-child查找
table_text4 = driver.find_element_by_css_selector('div#B div:nth-child(1)').text
# print(table_text4)

print('***********')
# 子节点定位父节点
table_text5 = driver.find_element_by_xpath("//div[@id='B']/..").text
# print(table_text5)







driver.quit()




