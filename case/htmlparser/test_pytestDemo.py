#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/15 19:18
# @Author : xurq
# @Site : 
# @File : pytestDemo.py
# @Software: PyCharm

import requests
import json

class Test_Demo:
    # def test_py1(self):
    #     payload = {'level':1,'name':'seveniruby'}
    #     r = requests.get('http://httpbin.testing-studio.com/get',params=payload)
    #     print(r)
    #     print(r.text)
    #     assert r.status_code == 200
    #
    def test_py2(self):
        payload = {"level":1,"name":"seveniruby"}
        r = requests.post('http://httpbin.testing-studio.com/post',data=payload)
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200


    def test_login(self):
        print('post2')
        header={"Content-Type":"application/json","accToken":"961e069542274dd28df13700f610a979",
                "systemId":"BMS",'serialNo':'694144113272'}

        payload={"password":"96qyVNn/porDY","userId":"XIZQ"}
        r=requests.post('https://testbmssit03.yylending.com/plms-um-service/http/user/login',headers = header,data=json.dumps(payload))
        print(r.status_code)
        print(r.text)
        # print(r.json())
        assert r.status_code==200



