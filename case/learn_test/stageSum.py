#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/11 19:11
# @Author : xurq
# @Site : 
# @File : stageSum.py
# @Software: PyCharm

salves = int(input('please input your salves:'))
bonus10 = 100000 * 0.1
bonus20 = bonus10 + 100000 * 0.075
bonus40 = bonus20 + 200000 * 0.05
bonus60 = bonus40 + 200000 * 0.03
bonus100 = bonus60 + 400000 * 0.015

if salves <= 100000:
    bonus = salves * 0.1
elif salves <= 200000:
    bonus = bonus10 + (salves - 100000)*0.075
elif salves <= 400000:
    bonus = bonus20 + (salves - 200000)*0.05
elif salves <= 600000:
    bonus = bonus40 + (salves - 400000)*0.03
elif salves <= 1000000:
    bonus = bonus60 + (salves - 600000)*0.015
else:
    bonus = bonus100 + (salves - 1000000)*0.01

print('your bonus is :%d'%bonus)





