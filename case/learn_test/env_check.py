import os
import time
import random


# 获取系统环境变量信息

confdir = os.getenv('PATH')
confdir1 = os.getenv('CLASSPATH')
# print(confdir)
# print('**********')
# print(confdir1)

# os.environ取出所有环境变量
env_list = os.environ
# 用get方式取得值
CLASSPATH = env_list.get('CLASSPATH')
# print('CLASSPATH=' + CLASSPATH)
# # 用字典方式取值
# JAVA_HOME = env_list['JAVA_HOME']
# print('JAVAHOME=' + JAVA_HOME)
# # 遍历所有的环境变量并将对应变量值打印出来
# for i,key in enumerate(env_list):
#     print(key + ':' + env_list[key])


# 大写转小写
l = [chr(ch) for ch in range(65,97)]
print(l)
l1 = []
for i in range(len(l)):
    if ord(l[i]) >= 65:
        up_l = ord(l[i]) + 32
        l1.append(chr(up_l))
print(l1)

l2 = [n for n in range(1,20)]
print(l2)
# 静态对象调用shuffle方法
random.shuffle(l2)
print(l2)

# **表示取幂
a = 2**8
print(a)


a,b,c = 'list1','list2','list3'
print(a,b,c)

mytuple = 4,5,6
print(mytuple)
x,y,z = mytuple
print(x,y,z)
