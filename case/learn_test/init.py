import operator
from collections import Counter

#我们定义一个Box类，有width, height, depth三个属性，以及计算体积的方法
class Box:
    #通过自定义方法初始化类属性
    def setDimension(self,width,heigth,depth):
        self.width = width
        self.heigth = heigth
        self.depth = depth
    def getVolume(self):
        return self.width * self.width * self.depth

#实例化类Box
b = Box()
b.setDimension(10,10,10)
bb = b.getVolume()
# print(bb)
# print(b.width)


class paper:
    def __init__(self,widths,higths,depths):
        self.widths = widths
        self.higths =higths
        self.depths = depths
    def getVolumes(self):
        return self.widths * self.higths * self.depths

#实例化,直接实例化的时候传入参数初始化,__init__()相当于一个构造器,类似于C++的 constructor
# p = paper(5,5,5)
# pp = p.getVolumes()
# print(pp)
# print(p.widths)




# strtest = 'hell o world!'
# print(strtest[0])
# print(strtest.find('e'))
# print(strtest.split())
# print(strtest.capitalize())
# print(strtest.title())
# print(strtest.count('o'))
#
# res='{name} {age} {sex}'.format(sex='male',name='egon',age=18)
# print(res)

list1 = [2,3,7]

tuple1 = (1,3,5)
tuple2 = (1,3)
# print(tuple1[0:2])
# print(len(tuple1))
# print(max(tuple1))
# print(tuple(list1))

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
#tup3 = tup1 + tup2
# print(tup3)
# print(tup1[1:5])
#print(tup1[0])

# for i in tup1:
#     print(i)

a = 'abcdefg'
#print(tup3[1:3])

list2 = list(tup3[0:1])
# print(list2)
# print(operator.eq('hello','hell'))

#冒泡排序
# nums = input("请输入：")
# def bouble_sort(nums):
#     num_list = list(nums)
#     print(len(nums))
#     print(num_list)
#     print(len(num_list))
#     num = list(set(num_list))
#     n = len(num_list)
#     for i in range(n - 1):
#         for j in range(0,n - i -1):
#             if num[j] > num[j + 1]:
#                 temp = num[j]
#                 num[j]= num[j+1]
#                 num[j+1] = temp
#     print(num)
#     num_sort = list(set(num))
#     return num_sort
#
# print(bouble_sort(nums))


#nums2 = [9,8,6,4,2,1]
#nums2 = input("please input :")
#nums2_list = list(map(int,list(nums2)))
# num3 = list(set(nums2))
# num3.sort()
#print(num3)



# nums = input("请输入：")
# def bouble_sort(nums):
#     print(nums)
#     num = list(nums)
#     print(num)
#     n = len(nums)
#     for i in range(n - 1):
#         for j in range(0,n - i -1):
#             if num[j] > num[j + 1]:
#                 temp = num[j+1]
#                 num[j+1]= num[j]
#                 num[j] = temp
#     #num_sort = set(num)
#     return num
#
# print(bouble_sort(nums))

# 列表中哪些存在于字典，哪些不存在于字典里
names = ['jj','jj1','jj2','wayne','jj lin']
languages = {'jj':'python','jj lin':'c','lin jj':'python'}
print(languages.keys())
for i in range(len(names)):
    if names[i] in languages.keys():
        print('thanks for ' + names[i])
    else:
        print('please join us '+ names[i])





# area_rivers = {'river1':'country1','river2':'country2','nile':'egypt'}
# for river,country in area_rivers.items():
#     print('The ' + river.title() + ' runs through ' + country.title())
#     print('The river name is ' + river.title())
#     print('Thd country name is ' + country.title())
#


#try except Exception捕获异常
# while True:
#     print('please input two numbers,and I will devide them!')
#     print("Enter 'q' to quit!")
#     first_num = input('\nthe first num:')
#     if first_num == 'q':
#         break
#     second_num = input('\nthe second num:')
#     if second_num == 'q':
#         break
#     try:
#         result = int(first_num) / int(second_num)
#     except ZeroDivisionError:
#         print('You can not devide by 0!')
#     else:
#         print(result)

#字符串做分隔后添加到字典中
# str_dic = []
# str = 'sadsfdsafdf,dsfd,lll,iookl'
# str_nums = str.split(',')
# print(len(str_nums))
# print(str.split(',',2)[1])
# for i in range(3):
#     str_dic.append(str.split(',',3)[i])
# print(str_dic)


# print(True + False)
# print(False)
#
# print(list(range(6)))
#
# classmates = ['Michael', 'Bob', 'Tracy']
# classmates.pop()
# print(classmates)
# try:
#     print(classmates[3])
# except IndexError:
#     print('default')


# 如果只有一个字符串元素，记得末尾加上,因为字符串是一个list
classmates1 = ('lilei',)
print(classmates1[0]) # lilei

# 这样定义的话，会把lilei当做一个字符串，取下标0的话打印的是l
classmates2 = ('lilei')
print(classmates2[0])

# 切片
a = list(range(10))
print(a[0:5])  # 从下标为0开始取5位[0, 1, 2, 3, 4]
print(a) # 取全部 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[:]) #取全部 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# d.pop('Michael')
# del d['Bob']
print(d.values())
if 75 in d.values():
    print('Bob')
else:
    print('no')

for item in d.values():
    print(item)

for i,item in enumerate(d):
    print(i,item,d[item])

s = set([1,2,3])
print(s)

print(id(s))



dd = {'4': 3,'3': 2,'17': 2,'17':1}
print(dd)
print(Counter(dd))

ss = 'abcbcaccbbad'
print(Counter(ss))

ll = ['a','b','c','c','a','b','b']
print(Counter(ll))







