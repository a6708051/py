# -* - coding: UTF-8 -* -
import urllib.request
import http.cookiejar

url = "https://www.lieshow.com/Login/check_account"

postdata = urllib.parse.urlencode({
	"account":"kary"
	}).encode('UTF-8')

headers = {
	"Accept":"application/json, text/javascript, */*; q=0.01",
	"Accept-Encoding":"gzip, deflate, br",
	"Accept-Language":"zh-CN,zh;q=0.8",
	"Cache-Control":"no-cache",
	"Connection":"keep-alive",
	"Content-Length":"12",
	"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
	"Cookie":"PHPSESSID=78d274457322e73c351124774054f4ab",
	"Host":"www.lieshow.com",
	"Origin":"https://www.lieshow.com",
	"Pragma":"no-cache",
	"Referer":"https://www.lieshow.com/Login/",
	"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
	"X-Requested-With":"XMLHttpRequest",
}

req = urllib.request.Request(url, data=postdata, headers=headers)
print (urllib.request.urlopen(req).read().decode('UTF-8'))

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open(req)
print (r.read().decode('UTF-8'))
