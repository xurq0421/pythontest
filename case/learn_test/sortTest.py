#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/17 15:30
# @Author : xurq
# @Site : 
# @File : sortTest.py
# @Software: PyCharm

# 按sort方法排序，然后从最后一个元素开始判断，去重
list1 = [5,4,3,6,7,8,0,9,1,2,3,4,5,5,4,3]
list1.sort()
len1 = len(list1)
last = list1[-1]
for i in range(len1-2,-1,-1):
    if last == list1[i]:
        del list1[i]
    else:
        last = list1[i]
print(list1)

list2 = [5,4,3,6,7,8,0,9,1,2,3,4,5,5,4,3]
list2.sort()
list3 = []
n2 = len(list2)
for i in range(n2-1,-1,-1):
    if list2[i] not in list3:
        list3.append(list2[i])
print(list3)






