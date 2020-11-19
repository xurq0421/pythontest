#!/usr/bin/env python
#coding=utf-8
import os
from time import strftime,time
import zipfile

# -*- coding: utf-8 -*-
# @Time : 2020/6/9 16:27
# @Author : xurq
# @Site : 
# @File : logs.py  搜索指定目录下的所有*.log文件，并且压缩以日期格式上传
# @Software: PyCharm

# dir = 'D:\case\learn_test'
# zip_name = './' + strftime('%Y-%m-%d') + '.zip'
# zip = zipfile.ZipFile('./88.zip','w',zipfile.ZIP_DEFLATED)

# for path,dirs,files in os.walk(dir):
#     print(path)
#     for file in files:
#         file_name,file_ext = os.path.splitext(file)
#         if file_ext == '.txt':
#             zip.write(os.path.join(path,file))
# zip_list = zip.namelist()
# for f in zip_list:
#     print(f)
#     zip.extractall('D:\case\learn_test\\test')
# zip.close()

txt_dir = 'D:\case\learn_test'
zip_file = zipfile.ZipFile('./666.zip','w',zipfile.ZIP_DEFLATED)

dirs_list = os.listdir(txt_dir)
for dir in dirs_list:
    print(dir)

for path,dirs,file_names in os.walk(txt_dir):
    pathname = os.path.abspath('.')
    f_path = path.replace(pathname,'')
    for file_name in file_names:
        root_name,file_ext = os.path.splitext(file_name)
        if file_ext == '.txt':
            zip_file.write(os.path.join(path,file_name),os.path.join(f_path,file_name))
zip_list = zip_file.namelist()
print(zip_list)
# zip_lists = zip_file.infolist()
# print(zip_lists)
for file in zip_list:
    print(file)
    savePath = "D:\case\learn_test\\test\\" + file
    f = open(savePath,'wb')
    f.write(zip_file.read(file))
    f.close()
zip_file.close()




# zip = zipfile.ZipFile('./33.zip', 'w', zipfile.ZIP_DEFLATED)
# for path, dir_names, file_names in os.walk(dir):
#     # 去掉目标和路径，只对目标文件夹下边的文件及文件夹进行压缩（包括父文件夹本身）
#     this_path = os.path.abspath('.') # 当前目录的绝对路径
#     fpath = path.replace(this_path, '')
#     for filename in file_names:
#         # path全路径，fpath当前路径，找到全路径下的所有文件，按照当前绝对路径进行压缩
#         file_name,file_ext = os.path.splitext(filename)
#         if file_ext == '.txt':
#             zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
# zip.close()







# 压缩当前目录下的文件，不涉及子目录
# for file in os.listdir(dir):
#     file_name,file_ext = os.path.splitext(file)
#     if file_ext == '.txt':
#         zip.write(file)
# zip_list = zip.namelist()
# for f in zip_list:
#     zip.extract(f,'D:\case\learn_test\\test')
# zip.close()


# def get_zip(files, zip_name):
#     zp = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
#     for file in files:
#         zp.write(file)
#     zp.close()
#     time.sleep(5)
#     print('压缩完成')
#
# if __name__ == '__main__':
#     # 文件的位置，多个文件用“，”隔开
#     files=['./report.html','./report.txt']
#     # 压缩包路径及名字
#     zip_file = './66.zip'
#     get_zip(files,zip_file)

# unZipPath = ''
# unZipPath = os.path.splitext('D:\case\learn_test\\test')[0]
# print(unZipPath)






