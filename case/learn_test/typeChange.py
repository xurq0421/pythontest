#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/9 18:42
# @Author : xurq
# @Site : 
# @File : typeChange.py
# @Software: PyCharm

# 单列集合中的元素是双列的可以转换成列表
strList1 = [(1,2),(4,5)]
strList2 = ['a','b']
# 列表转字典
print(dict(strList1))

strList11 = [1,2,4,5]
# print(dict(strList11)) #单列元素会报错

# 字典转列表
strDict1 = {'a':1,'b':2,'c':3}
# 默认只会转换key值到列表
print(list(strDict1))
# 转换成元组列表
print(list(strDict1.items()))


print(int('1111',2))
print(int(0b1111))
# 十进制转二进制
print(bin(15))
# 十六进制转二进制
print(bin(0x10))
# 八进制转二进制
print(bin(0o11))

print('二进制转八进制:',oct(0b11))
print('十进制转八进制',oct(10))
print('十六进制转八进制',oct(0x10))


