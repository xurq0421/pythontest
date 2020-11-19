#coding=utf-8

from LASInterface import LASInterface
import unittest

class Test_LAS(unittest.TestCase):
    def test_las_sumbit(self):
        # print('test_las_submit')
        #秒贷接口测试
        LASInter = LASInterface('https://testlassit02.yylending.com','MiaoDai')
        LASInter.modifyInnerCreditLog('00054a9b54e14a8da6a1af397da0f9e7','SIT01','innereval')
        LASInter.getSmsCode()
        LASInter.toRegister()
        LASInter.toLogin()
        LASInter.inviteCode('000030')
        print('call invitecode')
        LASInter.getData()
        LASInter.selectDBdata()




class TestAdd(unittest.TestCase):
    def setUp(self):
        print('test start')

    def Count(self,a,b):
        return 2+3
    def test_add(self):
        j = TestAdd.Count(self,2,3)
        # self.assertEqual(j.add(), 6, '计算错误！')
        self.assertEqual(j,6)

    def tearDown(self):
        print('test end')







