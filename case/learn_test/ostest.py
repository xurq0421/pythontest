import argparse
import os
import string

#批量命名指定目录下所有文件的后缀

# 从命令行接收参数并打印
# parser = argparse.ArgumentParser()
# parser.add_argument("-e","--echo",help="这是一段注释")
# args = parser.parse_args()
# print(args.echo)

path_01 = 'D:\case\learn_test\wether.csv'
path_02 = 'D:\case\learn_test\\test_result.txt'
file = os.listdir('D:\case\learn_test')# 列出目录下所有的文件
# print(file)
# 分离文件名与后缀名
res_01 = os.path.splitext(path_01)
res_02 = os.path.splitext(path_02)
# print(res_01[1])
# print(res_02[0])
# 返回路径和文件名
dirname,filepath = os.path.split(path_01)
# print(dirname)
# print(filepath)

# 将分离的合成一个整体
filename = os.path.join('D:\case\learn_test\\','wether.csv')
# print(filename)


# split()函数
# string.split(str='',num=string.count(str))[n] count()方法用于统计字符串里某个字符出现的次数
# str 分割符，默认为所有的空字符，包括空格，换行\n，制表符\t等
# num 分割次数
# n 选择第n个分片

string1 = 'hello.world.python'
# print(string1[0])
# print(string1.split('.'))# 以.为分割符 返回列表
# print(string1.split('.',1)) # 以.为分割符，分割2次['hello', 'world.python']
# print(string1.split('.',2)[1])# 以.为分割符，分割2次，取第2个分片 返回world

string2 = 'hello<python.world>and<c++>end'
# print(string2.split('<')[2].split('>')[0])# 输出c++




