#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/29 9:16
# @Author : xurq
# @Site : 
# @File : ReTest.py
# @Software: PyCharm

import re

def Find(string):
    # findall() 查找匹配正则表达式的字符串
    url = re.findall('https+://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    # url = re.findall('(do?)',string)
    return url


string = 'Runoob 的网页地址为：https://www.runoob.com，Google 的网页地址为：https://www.google.com'
# string = 'dfoesdoxydo'
print("Urls: ", Find(string))


print(re.findall('http?://w?','Runoob 的网页地址为：http://www.runoob.com，Google 的网页地址为：ftp://www.google.com,http://ww'))








