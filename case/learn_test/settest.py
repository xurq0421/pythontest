#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/24 9:04
# @Author : xurq
# @Site : 
# @File : settest.py
# @Software: PyCharm

import sys

list1 = set()
list1.add(123)
list1.add(456)
list1.add(789)

list2 = {'ddd','xxx','jjj','jjj'}
tuple1 = (666,777)
str1 = 'string'

dict_c = {'a':'111'}
list1.update(dict_c)
list1.update(list2)

# add是把变量元素当作一个整体添加到集合中
# list1.add(tuple1)
# list1.add(str1) # {'string', 'ddd', 456, (666, 777), 789, 'a', 'xxx', 'jjj', 123}

# update是把变量的元素拆开来添加到集合中
list1.update(tuple1)
list1.update(str1)  # {'jjj', 'r', 456, 777, 's', 'ddd', 789, 666, 'a', 'n', 't', 'i', 'g', 'xxx', 123}

list1.update({'xrq':'30'})
print(list1)

list1.remove('xrq')
list1.remove(789)
print(list1)



set1 = list1.copy()
print(set1)

set3 = {777,'ddd','bbbbbb'}


set2 = set.intersection(set1,set3)
print(set2)
print(set1&set3)
print(set1|set3)

def sss():
    thisset = set({"Google", "Runoob", "Taobao", "Facebook"})
    print(len(thisset))
    print('------------------------')
    if 'Taobao' in thisset:
        return True

    print('hello sss')
print(sss())

# print(thisset)
# x = thisset.pop()
# print(x)
# print(thisset)

a = set('abracadabra')
b = set('alacazam')

# print(a)
# print(b)
# print(a-b)
# print(b-a)
#
#
#
# c = {x for x in 'abcdefg' if x not in 'abc'}
# print(c)


strs = 'str'

l_list = [1,2,3,4,5,6,7]
# 7位数 每隔2位取一次，step不能为0，否则报错ValueError: slice step cannot be zero
# print(l_list[0:7:2])
# #　倒序取每一个数
# print(l_list[::-1])
# print(l_list[:-1])

del l_list
try:
    print(l_list)
except Exception as NameError:
    print('l_list is del!')


t = 123,456,'hello'
print(type(t))
# 输出的时候会把括号加上
print(t)

print(sys.path)

# 用sum函数实现数组元素之和
arr = [1,3,5,9,6]
print(sum(arr))
# 将数组首尾元素调换，在不知道元素个数的情况下用arr[-1]指的是倒数第一个元素
arr[0],arr[-1] = arr[-1],arr[0]
print(arr)

arr.sort()
print(max(arr))

del arr[1]
print(arr)


