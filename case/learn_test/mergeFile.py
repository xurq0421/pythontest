#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/9 19:45
# @Author : xurq
# @Site : 
# @File : mergeFile.py
# @Software: PyCharm
import os



fp1 = open('D:\\pythonFile\\test1.txt','r')
readStr1 = fp1.read()
fp1.close()
# print(type(readStr1))
print(readStr1)
fp2 = open('D:\\pythonFile\\test2.txt','r')
readStr2 = fp2.read()
fp2.close()
print(readStr2)
fp3 = open('D:\\pythonFile\\test3.txt','w+')
strL = list(readStr1+readStr2)
str = sorted(strL)
print(str)
strS = ''
strS = strS.join(str)
print(strS)
fp3.write(strS)
fp3.close()



