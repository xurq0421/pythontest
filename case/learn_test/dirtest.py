#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/5 15:52
# @Author : xurq
# @Site : 
# @File : dirtest.py
# @Software: PyCharm

import os
print(os.getcwd())
print(os.path.abspath('D:/case/learn_test/dirtest.py'))
print(os.path.dirname('D:/case/learn_test/dirtest.py'))
# 在python3中，os.path.walk要被os.walk取代了，尽量用os.walk
# print(os.path.walk('D:/case/learn_test/dirtest.py'))
print(os.walk('D:\case\\test'))




print(os.name)

print('-----------')
# for paths,dirs,files in os.walk('D:\case\\test'):
#     print(paths,dirs,files)


list1 = [3,2,2,4,1,1,6,5,5,8,9]
# list2 = set(list1)
# print(list2)
list1.sort()
print(list1)
len1 = len(list1)
last = list1[-1]
for i in range(len1-2,-1,-1):
    if last == list1[i]:
        del list1[i]
    else:
        last = list1[i]
print(list1)


nums = [1,2,3,4,5,6,7,5]
n = nums.index(5)
print(n)
print(nums[n+1:])


