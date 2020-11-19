#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/19 15:11
# @Author : xurq
# @Site : 
# @File : readtest.py
# @Software: PyCharm
import math
import random
from random import shuffle
import calendar

with open('D:\case\htmlparser\\test.txt','r') as fp:
    # text = fp.read()
    # print(type(text))
    print(fp.read())
    print(fp.read())

print('------')
with open('D:\case\htmlparser\\test.txt','r') as fp:
    print(fp.readline())
    print(fp.readline())
    print(fp.readline())

print('------')
with open('D:\case\htmlparser\\test.txt','r') as fp:
    text = fp.readlines()
    print(type(text))
    print(fp.readlines())

print('~~~~~~~~~~~~~')
def f(x):
    return x**2
res = map(f,[1,2,3,4,5])
list2 = []
for i in res:
    if i > 10:
        list2.append(i)
print(list2)


total = sum(range(1,101))
print('总和 = %d'%total)
average = total/100
print('平均 = %f'%average)


a = 'while i can'
b = a.capitalize()
print(a)
print(b)




a = 'abcdefg /ax b r a /'
b = a.split(' ',1)
c = b[0].upper() + b[1]
print(b)
print(c)

d = 'while i can'
e = d.split(' ',1)
f = e[0].upper()
print(f)


x = [chr(i) for i in range(97,123)]
print(x)
l1 = []
for i in x:
    l1.append(chr(ord(i) - 32))

print(l1)

y = str(x)
# print(y.upper())



# 97-122 a-z
# print(ord('a'))
# print(ord('z'))

# 65-90 A-Z
# print(ord('A'))
# print(ord('Z'))

print('******')
# 首字母大写，其余变小写
def normallize(name):
    return name.capitalize()
L1 = ['AdmIn','anny','LUCY','sandY','wILl']
L2 = list(map(normallize,L1))
# print(L2)

# 判断字符串里的大写字母转换为小写，小写转换为大写
str1 = 'While I Can'
xx = list(str1)
for i in range(len(xx)):
    if 96 < ord(xx[i]) < 123:
        xx[i] = chr(ord(xx[i]) - 32)
    elif 64 < ord(xx[i]) < 91:
        xx[i] = chr(ord(xx[i]) + 32)
yy = ''.join(xx)
print(yy)


print('水仙花数：')
for n in range(1,10):
    a1 = n*n*n
    for m in range(0,10):
        b1 = m*m*m
        for l in range(0,10):
            c1 = l*l*l
            abc = a1 + b1 + c1
            # print('abc = %d'%abc)
            w = n*100 + m *10 + l
            # w = '%d' % n + '%d' % m + '%d' % l
            # print('w = %d'%w)
            if abc == w:
                print(w)

print('三位数有：')
# 1，2，3能组成多少个互不相同且无重复数的三位数
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and j != k and i != k:
                print(i,j,k)

# 一个整数加上100是一个完全平方数，再加上168又是一个完全平方数，求这个整数
print('这个完全平方数是：')
for i in range(1,100):
    x = int(math.sqrt(i+100))
    y = int(math.sqrt(i+100+168))
    if (x*x == i+100) and (y*y==i+100+168):
        print(i)

# 任意输入三个整数，按从小到大顺序输出
# list_num = []
# for i in range(0,3):
#     a = input('请输入一个整数：')
#     list_num.append(a)
#
# list_num.sort()
# list_str = ''.join(list_num)
# print(list_str)

# A元素复制到B元素
print('复制后的元素：')
a = [4,5,8,7,8,9,6,5]
b = a[:]
print(b)

# 找到2000到3200年里所有能被7整除，不能被5整除的数，按逗号分隔的顺序打印在一行上
print('能被7整除不能被5整除的数是：')
# num_list = []
for i in range(2000,3201):
    if (i%7 == 0 and i%5!=0):
        print(i,end=',')
        # num_list.append(i)
# print(num_list)

# 编写一个可以计算给定数的阶乘的程序。结果应该以逗号分隔的顺序打印在一行上。假设向程序提供以下输入:8 则输出为:40320
print('阶承是：')
def jiecheng(num):
    if num == 0:
        return 1
    return num * jiecheng(num-1)
print(jiecheng(8))

# 使用给定的整数n，编写一个程序生成一个包含(i, i*i)的字典，该字典包含1到n之间的整数(两者都包含)。然后程序应该打印字典
# print('该字典是：')
# n = int(input('请输入一个整数：'))
# dict1 = dict()
# for i in range(1,n+1):
#     dict1[i] = i*i
# print(dict1)

# map用法,map py2.0返回列表，py3.0返回的是一个跌代器，需要用for循环获取结果
print('使用map的结果：')
def dd(num):
    return num**2
res = map(dd,[1,2,3,4,5,6])
for i in res:
    print(i,end=',')
print()

# 随机化列表
print('随机化列表后：')
name = ['lin jun jie','Lin JJ','JJ lin','Lin jie jie']
shuffle(name)
print(name)

# 如果有重复字符返回False,没有重复的返回true
print('判断结果：')
def uniqueChars(string):
    if string == '' or string == ' ':
        return False
    else:
        str1 = set(string)
        return len(string) == len(str1)
print(uniqueChars('1223'))

# 反转字符数组
print('反转后的结果：')
l9 = [1,2,3,4,5,6]
l8 = l9[::-1]
print(l8)

# 写算法实现字符数组反转
print('反转后的结果：')
l9 = [1,2,3,4,5,6]
l8 = []
for i in range(len(l9)-1,-1,-1):
    l8.append(l9[i])
print(l8)

print('-----------')
# What?为什么有三个元素都变成了X，我们明明值赋了一个值啊？这是因为[row] * 3这个操作实际上没有复制row，而只是创建了三个object reference，
# 也就是board[0] board[1] board[2]这三个元素其实指向了同一个列表row，那么改变board[0][0]其实就是改变row[0]，也同时改变了board[1][0] board[2][0]
row = ['*']*3
board = [row]*3
board[0][0]='x'
print(row)
print(board)

print('解释器解释数字：')
a = 256
b = 256
print(a is b)

a = 257
b = 257
print(a is b)

print('是否为闰年：')
print(calendar.isleap(2020))

# 有三个小偷，a说我不是小偷，b说c是小偷，c说d是小偷，d说c胡说
print('小偷是：')
for x in ('a','b','c','d'):
    sum = (x != 1)+( x == 'c')+(x == 'd')+(x != 'd')
    if (sum == 3):
        print(x)



