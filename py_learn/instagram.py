# -* - coding: UTF-8 -* -
import requests
import random
import http.cookiejar
import json
import info

class Instagram(object):
	def __init__(self):
		self.readCfg()

	def readCfg(self):
		with open('post.json') as json_file:
			data = json.load(json_file)
			self.url = data['post_url']
			self.headers = data['headers']

	def changeHeaders(self, new_headers):
		if (isinstance(new_headers, dict)):
			for key in new_headers:
				self.headers[key] = new_headers[key]

	def regist(self, post_data):
		#print (post_data)
		postdata = {"email":"hezong_changsha@sina.com","password":"hezong_changsha","username":"hezongchangsha","first_name":"yao"}
		res = requests.post(self.url, data=post_data, headers=self.headers)
		result = res.text
		
		print (res.text)

	def printHeaders(self):
		print (self.headers)


def test():
	info_center = info.InfoCenter('test.xls')
	info_data = info_center.getInfo()
	instagram = Instagram()
	instagram.regist(info_data)


if __name__ == '__main__':
	test()



'''
url = "https://www.instagram.com/accounts/web_create_ajax/"

postdata = {"email":"hezong_changsha@sina.com","password":"hezong_changsha","username":"hezongchangsha","first_name":"yao"}

headers = {
    'accept':'*/*',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.8',
    'cache-control':'no-cache',
    'content-length':'38',
    'content-type':'application/x-www-form-urlencoded',
    'cookie':'mid=WLpcDAAEAAEilI1gItV2TDnk1yFj; ig_vw=888; ig_pr=1; csrftoken=PolECgN381RQbIUUQweEd3lpV7cMnDj9',
    'origin':'https://www.instagram.com',
    'pragma':'no-cache',
    'referer':'https://www.instagram.com/',
    'user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'x-csrftoken':'PolECgN381RQbIUUQweEd3lpV7cMnDj9',
    'x-instagram-ajax':'1',
    'x-requested-with':'XMLHttpRequest',
}

res = requests.post(url, data=postdata, headers=headers)
print (res.text)
'''

