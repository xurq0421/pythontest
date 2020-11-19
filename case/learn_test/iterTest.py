#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/18 19:46
# @Author : xurq
# @Site : 
# @File : iterTest.py
# @Software: PyCharm

# 迭代器是访问集合元素的一种方法，它是可以记住遍历元素位置的对象，从集合的第一个元素开始访问，到最后一个
list = {1:50,2:30,3:40,4:60,5:70}
# 创建迭代器
it = iter(list)
print(next(it))
print(next(it))
print(next(it))

for i,key in enumerate(list):
    print(i,key,list[key])





