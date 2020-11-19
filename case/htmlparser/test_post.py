#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/18 10:32
# @Author : xurq
# @Site : 
# @File : test_post.py
# @Software: PyCharm


import requests
import json
class Test_Dome:
    def test_post(self):
        print('post2')
        header={'Content-Type':'application/json','accToken':'961e069542274dd28df13700f610a979',
                'systemId':'BMS','serialNo':'694144113272'}
        payload={"password":"96qyVNn/porDY","userId":"XIZQ"}
        r=requests.post('https://testbmssit03.yylending.com/plms-um-service/http/user/login',data=payload)
        print(r.status_code)
        print(r.text)
        # print(r.json())
        assert r.status_code==200


def tpost111():
    print('post1')
    header={'Content-Type':'application/json','accToken':'961e069542274dd28df13700f610a979',
            'systemId':'BMS','serialNo':'694144113272'}
    # payload={"password":"96qyVNn/porDY","userId":"XIZQ"}
    payload = {"level": 1, "name": "seveniruby"}

    r=requests.post('https://testbmssit03.yylending.com/plms-um-service/http/user/login',headers = header,data=payload)
    print(r.status_code)
    print(r.text)
    # print(r.json())
    assert r.status_code==200

# tpost111()