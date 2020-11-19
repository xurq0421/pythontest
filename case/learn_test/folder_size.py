import sys
import os



# sys.argv[]用来获取当前命令行正在执行的参数列表，[0]当前程序名，[1]第一个参数
# a = sys.argv[0]
# b = sys.argv[1]

# os.walk用来列出指定目录下的子目录以及子文件
allfiles = os.walk('D:\case')
dir_size = 0
for path,dirs,files in os.walk('D:\case'):
    for file in files:
        filename = os.path.join(path,file)
        dir_size += os.path.getsize(filename)

if dir_size == 0:
    print('file empty')
else:
    print('folder size is :' + str(dir_size) + ' bytes')




