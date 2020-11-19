#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/15 14:30
# @Author : xurq
# @Site : 
# @File : util.py
# @Software: PyCharm



# 凡是带有yield关键字的函数就是生成器
# foo()只是获取了一个生成器对象，并没有执行
# next(foo()) next对生成器执行操作，直至遇到yield停止执行
# 每次foo()只是获取了一个新的生成器(并产生了一个新的名称空间)而已，并没有执行
# g=foo() 先获得生成器对象
# next(g)执行生成器对象，直至遇到yield停止
# next(g)继续上一个操作继续执行，直至再次遇到yield停止执行

def foo():
    print('starting ......')
    while True:
        res = yield 4
        print('res:',res)
        yield 1
        print('ok1')
        yield 2
        print('ok2')

g = foo()
print(g)
print(next(g))
print('*'*20)
print(next(g))
print(next(g))
print(next(g))


def foo(num):
    print('starting...')
    while num<10:
        num=num+1
        yield num

for n in foo(0):
    print(n)





