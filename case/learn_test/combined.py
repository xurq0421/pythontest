#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/11 18:39
# @Author : xurq
# @Site : 
# @File : combined.py
# @Software: PyCharm

numList = [1,2,3,4]
# 生成无重复的两位数
count1 = 0
for i in range(1,5):
    for j in range(1,5):
        if i != j:
            print(i*10+j)
            count1 += 1

# 生成无重复的三位数
count2 = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and j != k and k != i:
                print(i*100+j*10+k)
                count2 += 1

# 生成无重复的4位数
count3 = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            for n in range(1,5):
                if i != j and j != k and k != n and n != i and i != k and j != n:
                    print(i*1000+j*100+k*10+n)
                    count3 += 1
count = count1 + count2 + count3

print('生成了%d个无重复数字！'%count)

# countt = 0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             for n in range(1,5):
#                 print(i*1000+j*100+k*10+n)
#                 countt += 1
# print('生成了%d个数字！'%countt)




