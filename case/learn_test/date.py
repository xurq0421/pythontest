#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/12 10:09
# @Author : xurq
# @Site : 
# @File : date.py
# @Software: PyCharm

year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))
days = 0
leap = 0

# 闰年：
if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
    leap = 1

months = [0,31,59,90,120,151,181,212,243,273,304,334]
if 0 < month <= 12:
    days += months[month - 1]
else:
    print('date error')
days += day

# 如果是闰年并且月份大于2月，天数加1
if (leap == 1) and (month > 2):
    days += 1

print('第%d天'%days)

# 闰年
# if leap == 1:
#     if month == 1:
#         days = day
#     elif month == 2:
#         days = 31+day
#     elif month == 3:
#         days = 60+day
#     elif month == 4:
#         days = 91+day
#     elif month == 5:
#         days = 121+day
#     elif month == 6:
#         days = 152+day
#     elif month == 7:
#         days = 182+day
#     elif month == 8:
#         days = 213+day
#     elif month == 9:
#         days = 244+day
#     elif month == 10:
#         days = 274+day
#     elif month == 11:
#         days = 305+day
#     else:
#         days = 335+day





