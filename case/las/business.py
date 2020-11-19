import requests
import json
import random
from collections import OrderedDict
import string
import unittest
import time
import linecache

# now = time.time()
# now = time.ctime()
# now = time.strftime("%Y-%m-%d-%H_%M_%S")
# path = now + 'html'
# print(now)

the_line = linecache.getline('d:/FreakOut.cpp', 222)
print (the_line)
# linecache读取并缓存文件中所有的文本，
# 若文件很大，而只读一行，则效率低下。
# 可显示使用循环, 注意enumerate从0开始计数，而line_number从1开始
def getline(the_file_path, line_number):
  if line_number < 1:
    return ''
  for cur_line_number, line in enumerate(open(the_file_path, 'rU')):
    if cur_line_number == line_number-1:
      return line
  return ''
the_line = linecache.getline('d:/FreakOut.cpp', 222)
print (the_line)


#随机生成多个手机号
# def phone_num(num):
#     phone_nums = set()
#     num_start = ['134', '135']
#     for i in range(num):
#         start = random.choice(num_start)
#         end = ''.join(random.sample(string.digits,8))
#         res = start + end + '\n'
#         print(res)
# phone_num(10)

# def phone():
#     num_start = ['131','132','133']
#     start = random.choice(num_start)
#     end = ''.join(random.sample(string.digits,8))
#     phone = start + end
#     return phone
# print(phone())

#测试
# chars = string.ascii_letters + string.digits
# print(chars)

url = 'https://testlassit01.yylending.com'

#获取短信验证码
# getSmsCode_url = '/las/basic/verify/getSmsCode'
# getSmsCode_data = {"mobile": phone(), "operation": "reg", "type": "1"}
# print(getSmsCode_data)
# header = {"version": "2.0", "source": "ios", "device": "FBC915C8-A13B-44D2-A1D0-E64E70E0F858", "aversion": "4.0.0.12",
#           "Content-Type": "application/json"}
# getSmsCode_res = requests.post(headers = header,url = url + getSmsCode_url,data = json.dumps(getSmsCode_data))
# print(getSmsCode_res.text)
#
# #注册
# toRegister_url = '/las/user/register/toRegister'
# toRegister_params = {"mobile":phone(),"password":"a1234567","verify":"123456","longitude":"12.3","latitude":"45.2"}
# toRegister_res = requests.post(headers = header,url = url+toRegister_url,data = json.dumps(toRegister_params))
# print(toRegister_res.text)
#
# #登录
# toLogin_path = '/las/user/login/toLogin'
# toLogin_params = {"mobile":"13505140002","password":"a1234567","longitude":"12.3","latitude":"45.2"}
# header = {"version": "2.0", "source": "ios", "device": "FBC915C8-A13B-44D2-A1D0-E64E70E0F858", "aversion": "4.0.0.12",
#           "Content-Type": "application/json"}
# toLogin_res = requests.post(url = url + toLogin_path,headers = header,data = json.dumps(toLogin_params))
# print(toLogin_res.text)
# toLogin_resDict = json.loads(toLogin_res.text)
# if toLogin_resDict['retCode'] == '000000':
#     print("登录成功!")

#退出登录
# toLogout_path = '/las/user/logout/toLogout'
# toLogout_res = requests.post(url = url + toLogout_path,headers = header)
# print(toLogout_res.text)


#有序字典
# languages = OrderedDict()
# languages['alice'] = 'a'
# languages['alin'] = 'b'
# languages['jen'] = 'c'
# languages['sun'] = 'd'
# for name,language in languages.items():
#     print(name + 'favorite language is ' + language)
#
# #创建30个红色的外星人
# aliens = []#创建一个空列表
# for alien_num in range(30):
#     new_alien = {'color':'red','points':'6','speed':'slow'}
#     aliens.append(new_alien)
#
# for alien in aliens[:6]:
#     print(alien)
# print('Total number of aliens: ' + str(len(aliens)))
