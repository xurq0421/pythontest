#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/9 14:05
# @Author : xurq
# @Site : 
# @File : copyList.py
# @Software: PyCharm
import time
import os


srcList = [4,3,5,6,7,2]
tarList = srcList[:]
print(srcList)

# 九九乘法表
# for i in range(1,10):
#     print(' ')
#     for j in range(1,i+1):
#         print('%d * %d = %d'%(i,j,i*j),end='  ')

# 暂停1秒输出
# myD = {'a':'1','b':'b'}
# for key,value in myD.items():
#     print(key,value)
#     # 格式化当前时间
#     print(time.strftime('%Y-%m-%d %H:%M:%S'))
#     time.sleep(1)


# 素数
# num = 0
# for m in range(101,200):
#     for n in range(2,m):
#         if(m%n==0):
#             break
#     else:
#         print(str(m) + 'is a 质数!')
#         num += 1
# print('一共有%d个质数!',num)


letters = 0
digit = 0
space = 0
others = 0
# strs = input('please input the strs:')
#
#
# #　isdigit判断是否是数字
# # isnumeric判断是否是数字字符串
# i = 0
# while i < len(strs):
#     c = strs[i]
#     i += 1
#     if c.isdigit():
#         digit += 1
#     if c.isspace():
#         space += 1
#     if c.isalpha():
#         letters += 1
# print(digit)
# print(space)
# print(letters)

print('---------------------')


ssss = [1,'1','一']
# print(ssss[0].isdigit())
print(ssss[1].isdigit())
print(ssss[2].isdigit())

print(ssss[1].isnumeric())
print(ssss[2].isnumeric())

print(ssss[1].isdecimal())
print(ssss[2].isdecimal())


k = 0
a = 1
while True:
    a = a*2 + 1
    k += 1
    if(k == 10):
        print(a)
        break


# 字符串相加，小写转大写
text = 'asda'
text += 'g'
c = ''
for i in text:
    if 97<= ord(i) <= 122:
        c += chr(ord(i) - 32)
print(c)


fileP = './date.py'
# 获取绝对路径
result = os.path.abspath(fileP)
print(result)

#　获取路径中的目录
result1 = os.path.dirname(result)
print(result1)

# 获取路径中的主体部分(最后的文件夹或文件名)
result2 = os.path.basename(result)
print(result2)

# 把一个完整路径分割成目录部分和主体部分
result3 = os.path.split(result)
print(result3)
#　分别获取目录部分和主体部分
re1,re2 = os.path.split(result)
print(re1)
print(re2)

# 把两个路径合并成一个
result4 = os.path.join(os.getcwd(),'666.zip')
print(result4)

# 把一个路径分割成目录部分和文件后缀部分，主要用于获取文件后缀,如果没有后缀名
# 就是空
result5 = os.getcwd() + '\\name.txt'
re3,re4 = os.path.splitext(result5)
print(re3,re4)



ddd = [({'a':'b'},(1,2))]

print(len(ddd))

kkk = ['aa','bbb',2,4]
for f in kkk:
    k = f
print(f)


