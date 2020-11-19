#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/7 13:40
# @Author : xurq
# @Site : 
# @File : rabbit.py
# @Software: PyCharm

# 有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月有多少对兔子？

# 月份   兔子数(对)            说明
# 1      1                   从开始有一对兔子
# 2      1                   第二个月还是一对兔子
# 3      1+1=2               第三个月开始生了一对兔子
# 4      1+1+1=3             第四个月又生了一对兔子
# 5      1+1+1+1+1=5         第五个月(第三个月新出生的兔子也满三个月了，也生了一对兔子)
# 6      1+1+1+1+1+1+1+1=8   最开始的一对生了一对，第三个月出生的兔子也生了一对，第四个月出生的兔子也满3个月了，出生了一对，再加上前5个月的兔子数 3对+5对=8对
# 所以兔子的数目序列是1 1 2 3 5 8 总结规律，前两项和等于第三项f(n) = f(n-2)+f(n-1)


def rabbit(n):
    # 第一个月为上个月f(n-2)
    last = 1
    # 第二个月为当前月f(n-1)
    now = 1
    # 第三个月为下一个月f(n)
    next = 0
    for i in range(1,n+1):
        # 如果是前两个月的话 每个月只有1对兔子
        if i <= 2:
            print('第%d个月有%d个兔子'%(i,1))
        # 从第三个月开始，下个月的兔子等于前两个月兔子之和
        else:
            # f(n) = f(n-2) + f(n-1)
            next = last + now
            # f(n-2) = now
            last = now
            now = next
            print('第%d个月有%d个兔子'%(i,next))
# rabbit(6)


# 求第n个月兔子的总对数
def deff(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return deff(n-1) + deff(n-2)

print(deff(5))  # 5个月总数

# 求阶承
def ddd(n):
    if(n == 1):
        return 1
    else:
        return n*ddd(n-1)
ddd(5)

# 2的n次方
def morrow(n):
    if n == 0:
        return 1
    else:
        return 2*morrow(n-1)
print('the result is :%d'%morrow(5))

# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
# 第一次弹起：100 + 50
# 第二次弹起：要先从50落下再弹起高度的一半就是50+50/2
# 第三次弹起：也要先从上上次的调度落下25再加上弹起的一半就是25+25/2
def countM(n):
    # 路径的总和
    sum = 0
    # 起始调度
    high = 100
    # high/2 每次跳回原来高度的一半
    # 经过的路径要加上落下的距离，就是high/2+high，这是每次经过的路径，假设原来经过的路径是sum，以后每次都要加上sum
    # 所以就是high + high/2 + sum，然后高度减半
    for i in range(n):
        sum = high + high/2 + sum
        high = high/2
    # 第十次落地时要减去最后一次跳起的高度，所以要减去最后的high/2
    sum -= high/2
    print('第十次反弹的距离总和：%0.2f'%sum)
countM(10)



