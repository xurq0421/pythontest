#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/18 10:14
# @Author : xurq
# @Site : 
# @File : md5test.py
# @Software: PyCharm
import hashlib

ss = '123456'
hs = hashlib.md5(ss.encode())
hm = hs.hexdigest()
print(hm)


# 倒序
list1 = [1,2,3]
list2 = []
i = len(list1)-1
while i >= 0:
    list2.append(list1[i])
    i -= 1
print(list2)

print(list1[::-1])
list1.reverse()
print(list1)
