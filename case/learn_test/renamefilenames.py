import argparse
import os

# 批量修改文件扩展名
def batch_rename(workdir,old_ext,new_ext):
    # 列出目录下所有的文件名
    filenames = os.listdir(workdir)
    # 遍历所有文件名，找出每一个文件的扩展名
    for filename in filenames:
        root_name,ext_name = os.path.splitext(filename)
        # 如果扩展名==old_ext,说明是需要更改的文件
        if ext_name == old_ext:
            # 给文件赋予新的名字
            newfile = root_name + new_ext
            # 重命名
            os.rename(os.path.join(workdir,filename),os.path.join(workdir,newfile))
    print(os.listdir(workdir))

# 命令行解析器函数
def get_parser():
    # 创建一个命令行解析器
    parse = argparse.ArgumentParser(description='change extension extname of files in the workdir')
    # 添加参数
    parse.add_argument('--workdir',help='workdir')
    parse.add_argument('--old_ext',help='old_ext_name')
    parse.add_argument('--new_ext',help='new_ext_name')
    # 解析参数 返回的是一个namespace
    args = parse.parse_args()
    batch_rename(args.workdir,args.old_ext,args.new_ext)
    # 解析参数，返回的是namespace类型，用args强转为字典类型，与上面方法功能一致
    # args = vars(parse.parse_args())
    # batch_rename(args['workdir'],args['old_ext'],args['new_ext'])

# 调用命令行解析器，命令行输入
get_parser()

# ['.idea', 'area_data.txt', 'baseData.py', 'bubble.py', 'classTest.py', 'fileTest.py', 'init.py', 'ostest.py', 'pi_digist.txt', 'randomtest.py', 'renamefilenames.py', 'report', 'test_result.txt', 'venv', 'wether.csv', '__pycache__']


# 创建10个以txt结尾的文本文件
# for i in range(10):
#     fn = 'D:\case\learn_test\\filetest\\' + str(i+1) + '.txt'
#     p = open(fn,'w+')