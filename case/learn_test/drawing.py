#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/7 14:52
# @Author : xurq
# @Site : 
# @File : drawing.py
# @Software: PyCharm

# def drawing(n):
#     for i in range(n/2):
#         print('*')

# rows = 7
# for i in range(rows):#变量i控制行数
#     for j in range(rows - i):#(1,rows-i)
#         print(' ',end=''),
#         j += 1
#     for k in range(2 * i - 1):#(1,2*i)
#         if k == 0 or k == 2 * i - 2:
#             print('*'),
#         else:
#             print(' ',end=''),
#         k += 1
#     # print('\n')
#     i += 1
#     #菱形的下半部分
# for i in range(rows):
#     for j in range(i):#(1,rows-i)
#         print(' ',end=''),
#         j += 1
#     for k in range(2 * (rows - i) - 1):#(1,2*i)
#         if k == 0 or k == 2 * (rows - i) - 2:
#             print('*'),
#         else:
#             print(' ',end=''),
#         k += 1
#     # print('\n')
#     i += 1

# for i in range(1,8,2):
#     print((i*'*').center(7))
# for i in reversed(range(1,6,2)):
#     print((i*'*').center(7))
#
# for i in range(1,8,2):
#     print('*'.center(6))

# s = '*'
# for i in range(1, 8, 2):
#     print((s * i).center(7))
# for i in reversed(range(1, 6, 2)):
#     print((s * i).center(7))

for i in range(10):
    for j in range(0,i):
        print("-",end='')
    for j in range(i, 10):
        print("$",end='')

    print()

# 等腰直角三角形
for i in range(10):
    for j in range(0,i):
        print('j ',end='')
    print()

for i in range(1,5):
    for j in range(5-i):
        print('$',end='')
    for k in range(2*i-1):
        print('*',end='')
    print()
for m in range(5):
    for n in range(m):
        print('$',end='')
    for p in range(2*(5-m)-1):
        print('*',end='')
    print()

for l in range(0):
    print(l,end='')

# 99乘法表
for i in range(1,10):
    for j in range(1,10):
        print('%d * %d = %d'%(i,j,i*j),end=' ')
    print()


for i in range(1,10):
 print("    ")
 for j in range(1, i+1):
     print('%d * %d = %d'%(i,j,i*j),end = ' ' )