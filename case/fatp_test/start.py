import unittest
import taizhanginfo
import fatplogin
import relateLoan
import os
import time
from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(fatplogin.Login('test_Login'))
suite.addTest(taizhanginfo.Taizhang_Info('test_Taizhang'))
suite.addTest(relateLoan.relate_loan('test_RelevanceLoanNos'))

#unittest.TextTestRunner().run(suit)


# dir = os.path.dirname(os.path.realpath(__file__))
# report_dir = '\Report'
# now_time = time.strftime('%Y-%m-%d %H_%M_%S')
# report_name = dir + report_dir + '\\' + now_time + 'result.html'
# print('++++++++++++++' + report_name)
#
# fp = open(report_name,"wb")
# runner = HTMLTestRunner(stream=fp,title='报告',description='用例执行情况')
# runner.run(suite)

#获取当前路径
dirc = os.path.dirname(os.path.realpath(__file__))
#添加一个子目录(手动在当前路径下创建一个Report文件夹)
report_dir = '\\Report'
#获取当前时间追加到文件名里
now_time = time.strftime('%Y-%m-%d %H_%M_%S')
report_path = dirc + report_dir + '\\' + now_time + 'result.html'

with open(report_path,'wb') as fp:
    runner = HTMLTestRunner(stream=fp,title='报告',description='用例执行情况')
    runner.run(suite)



































