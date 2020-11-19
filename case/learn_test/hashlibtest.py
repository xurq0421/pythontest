#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/14 15:11
# @Author : xurq
# @Site : 
# @File : hashlibtest.py
# @Software: PyCharm

import hashlib
import base64

str = 'JJLin JFJ'
str1 = str.encode(encoding='utf-8')
# MD5加密
str2 = hashlib.md5(str1)

# sha加密
m_sha224 = hashlib.sha224()
m_sha256 = hashlib.sha256()
print(m_sha224.hexdigest())
m_sha512 = hashlib.sha512()
print(m_sha256.hexdigest())
print(m_sha512.hexdigest())



# 作为二进制数据字符串加密
print(str2.digest())
# 作为十六进制数据字符串加密
print(str2.hexdigest())




# base64加密
print(base64.b64encode(str.encode()))
dd = base64.b64encode(str.encode())
# base64解密
bb = base64.b64decode(dd)
print(bb)
print(bb.decode())



a = [1, 2, 3, 4, 4, 5, 6, 7, 7, 9, 0]
a.sort()
b = []
# 按相反方向输出
last = a[::-1]
print(last)
for i in a:
    if i not in b:
        b.append(i)

print(b)

# 用循环的方式反向输出
n = len(a)-1
c = []
while n > 0:
    c.append(a[n])
    n -= 1
print(c)

print('------------------')
list1 = [1, 2, 4, 3, 4, 4, 5, 6, 7, 7, 9, 0]
list1.sort()
print(list1)
len1 = len(list1)
last = list1[-1]
# print(last)
for k in range(len1-2,-1,-1):
    if last == list1[k]:
        del list1[k]
    else:
        last = list1[k]

print(list1)