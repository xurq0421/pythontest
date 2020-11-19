#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/17 19:24
# @Author : xurq
# @Site : 
# @File : sortDict.py
# @Software: PyCharm


dic1 = {"b":"2","a":"1"}
dic2 = {"c":"2","a":"3"}

dic3 = sorted(dic1.items(),key=lambda key:key[1],reverse=False)

print(dic3)

