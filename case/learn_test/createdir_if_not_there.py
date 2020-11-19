import os
import Exception
# 如果文件夹不存在就创建文件夹，存在就提示目录已存在

MESSAGE = 'The Dir is arlready exist!'
testdir = 'testdir'
home = 'D:\case\learn_test\\filetest'

try:
    if not os.path.exists(os.path.join(home,testdir)):
        os.makedirs(os.path.join(home,testdir))
    else:
        print(MESSAGE)
except Exception as e:
    print(e)



