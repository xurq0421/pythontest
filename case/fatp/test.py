


import logging
import os
from taizhanginfo import Taizhang_Info
import json



#级别排序：critical > error > warning > info > debug 如果设置Debug将会把所有级别打印在控制台
log_path = os.path.dirname(os.path.realpath(__file__)) + '\\new.log'
#file = open(log_path,encoding="utf-8",mode="a")


# log_format = "%(asctime)s-%(levelname)s-%(message)s"
# logging.basicConfig(stream=file,level=logging.INFO,format=log_format)

# print(log_path)
#第一步，创建一个logger
# logger = logging.getLogger()
#y设置等级总开关
# logger.setLevel(logging.INFO)
#第二步，创建一个handler，用于写入日志文件
# fh = logging.FileHandler(log_path,mode='w')
# fh.setLevel(logging.INFO)
#第三步，定义handler的输出格式
# formatter = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# fh.setFormatter(formatter)
#将handler添加到logger里
# logger.addHandler(fh)

#logging.basicConfig(filename='new.log',level=logging.INFO,format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')

logging.basicConfig(level=logging.INFO,filename=log_path,filemode='a',format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# logging.basicConfig(level=logging.INFO,#控制台打印的日志级别
#                     filename= log_path,
#                     #stream=file,
#                     filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
#                     #a是追加模式，默认如果不写的话，就是追加模式
#                     format=
#                     '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
#                     #日志格式
#                     # handlers=[logging.StreamHandler()]
#                     )



# a = 10
# b = 0
# try:
#     c = a/b
# except Exception as e:
#     logging.info(e)
#     logging.debug(u"苍井空")
#     logging.info(u"麻生希")
#     logging.warning(u"小泽玛利亚")
#     logging.error(u"桃谷绘里香")
#     logging.critical(u"泷泽萝拉")
# print('done')

notpad_dir = '\\Notpad'
notpad_path = os.path.dirname(os.path.realpath(__file__)) + notpad_dir + '\\notpad.txt'
f = open(notpad_path,'wb')
tzinfo = Taizhang_Info()
tz_text = tzinfo.test_Taizhang()
f.writelines(tz_text)
#print(tz_dic)
f.close()
ff = open(notpad_path,'r',encoding='utf-8')
str = ff.read()

strr = json.loads(str)

# print(type(strr))
# logging.info(type(strr))

strrr = strr['data']['lmList']
# print(strrr)
# logging.info(strrr)
try:
    for str_dic in strrr:
        # print(str_dic)
        if (str_dic['applySerialNo'] == 'PA20200414000002' and strr['retCode'] == '000000'):
            logging.info('success!')
        else:
            logging.info('error')
except Exception as e:
    logging.INFO(e)

