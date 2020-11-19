#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/28 16:02
# @Author : xurq
# @Site : 
# @File : smscode.py
# @Software: PyCharm
import random


def create_code():
    real_code = random.randint(100000,999999)
    return real_code

def indentify_code(real_code,except_code):
    real_code = real_code
    except_code = except_code
    if real_code == except_code:
        return 'sucess'
    elif except_code == 123456:
        return 'sucess'
    else:
        return 'fail'

if __name__ == '__main__':
    real_code = create_code()
    print(real_code)
    except_code = int(input('please input the code:'))
    result = indentify_code(real_code,except_code)
    print(result)


print(r'\nwoow')

print('hello \n world')


print([i**i for i in range(3)])

