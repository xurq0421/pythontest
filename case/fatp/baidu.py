import requests

reponse = requests.get('https://www.baidu.com/')
print(reponse.text)
print(type(reponse.status_code),reponse.status_code)
print(type(reponse.headers),reponse.headers)
print(type(reponse.cookies),reponse.cookies)
print(type(reponse.url),reponse.url)
print(type(reponse.history),reponse.history)


