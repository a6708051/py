# -* - coding: UTF-8 -* -
import random
import xls

class InfoCenter(object):
	def __init__(self, xml):
		self.xml = xml
		self.xls_read = xls.XlsHandle(self.xml)

	def getRandValue(self):
		xls_attr = self.xls_read.readXlsRCs()
		if (xls_attr["rows"] > 1):
			rand = random.randint(1, xls_attr["rows"])
		else:
			rand = 0
		value = self.xls_read.readValue(rand, 2)
		return value

	def getInfo(self):
		data = {}
		data['first_name'] = self.getRandValue() + self.getRandValue()
		data['last_name'] = self.getRandValue()
		data['username'] = data['first_name'] + '_' + data['last_name']
		data['email'] = data['username'] + '@sina.com'
		data['password'] = 'pass_' + data['first_name'] + data['last_name']
		return data



def test():
	xls_read = InfoCenter('test.xls')
	info = xls_read.getInfo()
	print (info)

if __name__ == '__main__':
	test()
