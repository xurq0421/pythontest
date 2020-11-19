import requests
from fatplogin import Login
import unittest
import json
import logging

#设置日志打印级别
# logging.basicConfig(level=logging.INFO)

class Taizhang_Info(unittest.TestCase):
    def test_Taizhang(self):
        logininfo = Login()
        accToken = logininfo.test_Login()
        # print('return token :'+accToken)
        fatp_url = 'https://testfatpsit01.yylending.com/'
        taizhangPath = fatp_url + 'fatp-lm-service/http/lm/lonInformation/getLendgerDetail'
        taizhangdata = {
                "applySerialNo": ["PA20200414000002"],
                "loanNo": "LA20200414000001",
                "putOutStartDate": "",
                "putOutEndDate": "",
                "pageNum": 1,
                "pageSize": 10,
                "customerName": "黄滴烙"
                }
        taizhangHeader = {'Content-Type':'application/json','acctoken':accToken,'systemid':'FATP'}
        try:
            taizhangTest = requests.post(url=taizhangPath,data=json.dumps(taizhangdata),headers=taizhangHeader)
           # print(taizhangTest.content) #二进制
           # print('taizhang :' + taizhangTest.text)
            taizhangres_dict = json.loads(taizhangTest.text)
            if (not taizhangTest or taizhangres_dict['retCode'] != '000000'):
                print('error')
            return taizhangTest
        except Exception as e:
            logging.info('台账信息接口返回错误')



