#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/16 14:47
# @Author : xurq
# @Site : 
# @File : learntest.py
# @Software: PyCharm

import os

# 二分法
def binary_test(list1,num):
    low = 0
    high = len(list1)-1
    while low <= high:
        mid = (low + high) // 2
        temp = list1[mid]
        if temp == num:
            return mid
        elif temp > num:
            high = mid - 1
        else:
            low = mid + 1
    return None

# nums = [0,1,2,3,4,5,6,7,8,9]
# mid = binary_test(nums,0)
# print(mid)




# 列表排序后从最后一个元素判断，相同则删除
list2 =[5,6,8,7,1,4,5,9]
list2.sort()
# print(list2)
# [1, 4, 5, 5, 6, 7, 8, 9]
last = list2[len(list2)-1]
# print(last)
for i in range(len(list2)-1,-1,-1):
    if list2[i] == last:
        del list2[i]
    else:
        last = list2[i]
# print(list2)


def fab(n):
    a, b = 0, 1
    while n:
        yield b
        a, b = b, a+b
        n -= 1

g = fab(3)
print(next(g))
print(next(g))
print(next(g))

print('--------')

x,y = 1,1
x,y = y,x+y
print(x,y)

print('------')

for file in os.listdir('D:\case\htmlparser'):
    print(file)

print('-----------')
# 递归输出文件
def print_directory_contents(sPath):
    for sChild in os.listdir(sPath):
        print(sPath)
        print(sChild)
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)
print_directory_contents('D:\case\htmlparser')

print('***********')
# 列出指定路径下所有的目录，子目录以及所有文件
for path,dir,file in os.walk('D:\case\htmlparser'):
    # print(path,dir,file)
    print(path)
    print(dir)
    print(file)
    print('#$#$#$#$')



