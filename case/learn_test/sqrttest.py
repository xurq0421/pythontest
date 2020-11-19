#!/usr/bin/env python
import math
import random
# -*- coding: utf-8 -*-
# @Time : 2020/6/12 9:43
# @Author : xurq
# @Site : 
# @File : sqrttest.py
# @Software: PyCharm

# i是i+100的平方根，也是i+168的平方根，求i
for i in range(100000):
    x = int(math.sqrt(i+100))
    y = int(math.sqrt(i+168+100))
    if (x*x == i+100) and (y*y == i+168+100):
        print('i = ' + str(i))
        print('x = '+ str(x))
        print('y = ' + str(y))
print('--------------------------')

print(type(math.sqrt(100)))
print(math.sqrt(100))
print(math.sqrt(5))
print(math.pi)

# l = []
# for j in range(3):
#     j = int(input('input your num:'))
#     l.append(j)
#
# l.sort()
# print(l)

# print('*'*10)
# for i in range(5):
#     print('*        *')
# print('*'*10)
# print('*\n'*6)


cars = ['bmw','audi','toyota','subaru']
# reverse=True 正常排完序后再倒序
cars.sort(reverse=True)
print(cars)

buses = ['bmw','audi','toyota','subaru']
# sorted(buses)按特定顺序显示列表元素，但并不改变原列表顺序
print(sorted(buses))
print(buses)


l1="162"
l2=sorted(l1)
print(l2)

# 声明字典
key_value = {}

# 初始化
key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323

print(key_value)

# str = 'hello world'
# strList = list(str)
# print(strList)
# # print(list(enumerate(strList)))
# print(','.join(strList)) # 将字符串，列表，元组按指定分隔符输出



# for i,key in enumerate(strList):
#     print(i,key)

# 返回一个迭代器
sorted(key_value)
#　定义一个空字典，用于将排序后的 key value加入字典
dict_list = {}
# 字典按键排序
for key in sorted(key_value):
    # 排完序的key value分离了 (1, 2) (2, 56)
    print((key,key_value[key]))
    # 把排序好的key,value重新加入字典
    dict_list[key] = key_value[key]

print(dict_list)

# 按字典值排序
key_value_sorted = sorted(key_value.items(),key=lambda x:x[1],reverse=False)
print(key_value_sorted)
# 定义一个新的空的字典，用于将排序后的key value添加进来，返回的key_value_sorted是个list,可用于for循环
dic_sorted = {}
for k_v in key_value_sorted:
    dic_sorted[k_v[0]]=k_v[1]
print(dic_sorted)


list1 = [1,2]
list2 = [3,4]
print(list1+list2)

tup1 = (1,2)
tup2 = (3,4)
print(tup1+tup2)





