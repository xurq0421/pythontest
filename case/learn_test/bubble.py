import random

# def bubble(nums):
#     nLen = len(nums)
#     for i in range(nLen-1):
#         for j in range(i+1,nLen):
#             if nums[i] > nums[j]:
#                 nums[i],nums[j] = nums[j],nums[i]
#     numTemp = []
#     for k in nums:
#         if k not in numTemp:
#             numTemp.append(k)
#     return numTemp

# 使用逐个输入，逐个转换成int然后再添加进列表的方式全部转换成数字列表
# num = []
# while 1:
#     n1 = input('please input the nums:').strip()
#     if n1 == 'q':
#         break
#     else:
#         print(n1)
#         num.append(int(n1))
#         print(num)
# print(bubble(num))

# print(bubble([25,23,10,10,48,2]))

# 把字符串列表转换成数字列表
# xlist = ['56','45','10','12','5']
xlist = input('请输入数字，并用逗号隔开：').strip().split(',')
print(xlist)
# xlist = [int(xlist[i]) for i in range(len(xlist))]
# print(xlist)
# print(bubble(xlist))

# 二分查找
# def binary_search(list, item):
#     low = 0
#     high = len(list) - 1
#
#     while low <= high:
#         mid = int((low + high) / 2)
#         guess = list[mid]
#         if (item == guess):
#             return mid
#
#         if (guess > item):
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
#
#
# test_list = [1, 5, 5,10,10,10, 10,20, 90, 100]
# print(binary_search(test_list, 5))

# 包含10，输出0-10
# for i in range(10):
#     print(random.randint(0,10))




