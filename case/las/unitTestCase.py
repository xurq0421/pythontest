#coding=utf-8
import testLAS

from testLAS import Test_LAS
from testLAS import TestAdd
from HTMLTestRunner import HTMLTestRunner
import time
import os

if __name__ == '__main__':
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestAdd('test_add'))
    suite.addTest(Test_LAS('test_las_sumbit'))
    #按照一定格式获取当前时间
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    #获取当前路径
    nowPath = os.path.dirname(os.path.realpath(__file__))
    #print('nowPath :' + nowPath)
    #用文本格式看
    file = open('test_result.txt','a')
    #TextTestRunner实例化的Runner,文件打开方式不能是二进制的也就是'wb'
    runner = unittest.TextTestRunner(stream=file, descriptions='测试报告', verbosity=2)
    runner.run(suite)
    file.close()


    #用Html的格式看 print在控制台没有输出了
    #定义报告存放路径
    # filename = nowPath + '\\'+'report' + '\\' + now + 'result.html'
    # fp = open(filename,'wb')
    # #执行测试集合
    # testrunner = HTMLTestRunner(stream = fp,title = '测试报告',description = '测试用例执行情况：')
    # # HTMLTestRunner()
    # testrunner.run(suite)
    # fp.close()



