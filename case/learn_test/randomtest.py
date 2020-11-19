import random
import string

#使用for循环打印1-20(含)
# numlist = []
# for i in range(21):
#     numlist.append(i)
# print(numlist)

# num = '123'
# for i in range(len(num)):
#     print(random.randint(1,10))

#print(random.random())  # 随机浮点数，默认取0-1，不能指定范围
# print(random.randint(1, 20))  # 随机整数，顾头顾尾
# print(random.choice('sdfsd233'))  # 随机取一个元素
#print(random.sample('hello234234史蒂夫34', 4))#从序列中随机取几个元素,返回是一个list
#print(random.uniform(1, 9))  # 随机取浮点数，可以指定范围
# x = [1, 2, 3, 4, 6, 7]
# random.shuffle(x)  # 洗牌,打乱顺序，会改变原list的值
# print(x)

# def phone_num(num):
#     all_phone_nums=set()
#     num_start = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187', '188',
#            '147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']
#     for i in range(num):
#         start = random.choice(num_start)
#         end = ''.join(random.sample(string.digits,8))
#         res = start+end+'\n'
#         all_phone_nums.add(res)
#     with open('phone_num.txt','w',encoding='utf-8') as fw:
#         fw.writelines(all_phone_nums)
# phone_num(10)

# start_num = '135'
# num = ''.join(random.sample(string.digits,8))
# print(start_num + num)

#随机生成手机号
all_phone_nums = []
start_nums = ['131','132','133']
for i in range(10):
    start_num = random.choice(start_nums)
    # print(string.digits)
    end_num = ''.join(random.sample(string.digits,8))
    phone_num = start_num + end_num + '\r'
    print(phone_num)
    all_phone_nums.append(phone_num)
    phone_nums = set(all_phone_nums)
# print(phone_nums)
with open('phone_nums.txt','a',encoding='utf-8') as fw:
    fw.writelines(phone_nums)

#创建一个列表，包含1-1000000，求最大最小和总和
num_list = []
for i in range(1,1000001):
    num_list.append(i)
#print(num_list)
print('最小的数是：'+str(min(num_list)))
print('最大的数是：'+str(max(num_list)))
print('总和是：'+str(sum(num_list)))


#倒序
# str = input("please input the str:")
# str1 = []
# print(str[0])
#print(str[::-1]) #方法1：使用str[::-1]实现字符串倒序翻转

#方法2：使用for循环将str字符从末尾逐个添加到Str1中
# for i in range(len(str)-1,-1,-1):
#     str1.append(str[i])
# print(''.join(str1))

#方法3：使用list的函数reverse()进行倒序排列，然后再使用''.join()转为字符串
# list1 = list(str)
# list1.reverse()
# print(''.join(list1))

# str2 = ""
# for i in range(len(str1)-1,-1,-1):
#     str2 += str1[i]#将str1里的字符从末尾开始逐个添加到str2中
# print(str2)

# for i in range(10,-1,-1):
#     print(i)


# x = int(input('please input the first num:\n'))
# y = int(input('please input the second num :\n'))
# z = int(input('please input the third num:\n'))
#
# l = []
# l.append(x)
# l.append(y)
# l.append(z)
# l.sort()
# print(l)
#













