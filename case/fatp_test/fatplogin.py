import requests
import json
import unittest

#登录
class Login(unittest.TestCase):
	def test_Login(self):
		fatp_url = 'https://testfatpsit01.yylending.com/'
		login_path = fatp_url + 'plms-um-service/http/user/login'
		login_data = {"userId": "YANCFA",	"password": "96qyVNn/porDY","systemId": "FATP","source": "","macId": ""}
		login_header = {'Content-Type':'application/json'}

		# login_res = requests.post(url=login_path,headers=login_header,data=json.dumps(login_data))
		login_res = requests.post(url=login_path,headers=login_header,json=login_data)
		login_res_text = json.loads(login_res.text)
		print('status_code')
		print(login_res.status_code)
		#print(login_res_text)
		accToken = login_res_text['data']['accToken']
		retcode = login_res_text['retCode']
		if not login_res_text or retcode != '000000':
			print('error')
		print(accToken)
		return accToken


