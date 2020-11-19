#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/19 18:28
# @Author : xurq
# @Site : 
# @File : is_number.py
# @Software: PyCharm

import unicodedata
import time
import datetime

def is_number(num):
    try:
        float(num)
        print('one:' + num)
        print(type(float(num)))
        return True
    except ValueError:
        pass

    try:
        unicodedata.numeric(num)
        print('two' + num)
        print(type(unicodedata.numeric(num)))
        return True
    except(TypeError,ValueError):
        pass

    return False

# print(is_number('十'))


def is_num(n):
    unicodedata.numeric(n)
    print(n)

is_num('十')


# 求阶乘
# num = int(input('please input the num:'))
# factorial = 1
#
# # 判断是不是负数
# if num<0:
#     print('不能是负数，负数没有阶乘')
# elif num == 0:
#     print('0的阶乘为1')
# else:
#     for i in range(1,num+1):
#         factorial = factorial * i
#         print(factorial)
# print(factorial)

times = time.strftime('%Y-%m-%d %H:%M:%S')
print(times)

today = datetime.date.today()
yesterday = datetime.date.today() + datetime.timedelta(-2)

print('today is ' + str(today))
print('yesterday is ' + str(yesterday))


print(today - datetime.timedelta(days=1))











