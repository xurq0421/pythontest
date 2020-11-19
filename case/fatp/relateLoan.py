import requests
import unittest
import json

class relate_loan(unittest.TestCase):
    def test_RelevanceLoanNos(self):
        url = 'https://testfatpsit01.yylending.com/'
        relaloan_path = url + 'fatp-lm-service/http/lm/account/foreign/getBatchRelevanceLoanNos'
        header = {'Content-Type':'application/json'}
        data = {
	       "certIds": ["330411199106121678"	],
	       "customerIds": ["CT20200414000335"]
        }
        relate_res = requests.post(url=relaloan_path,data=json.dumps(data),headers=header)
        print('ralate : ' + relate_res.text)


