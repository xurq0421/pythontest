#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/13 19:09
# @Author : xurq
# @Site : 
# @File : testcase.py
# @Software: PyCharm

import json
import requests

def test_wk_json():
    r = requests.get('https://www.baidu.com/')
    print(r.text)


test_wk_json()



