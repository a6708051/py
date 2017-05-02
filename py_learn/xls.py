# -* - coding: UTF-8 -* -
import os
import xlrd
import xlwt
from xlutils.copy import copy

class XlsHandle(object):
	__read_book = None
	__xml_rows = 0
	__xml_cols = 0
	def __init__(self, xls):
		self.xls = xls
		self.readXls()

	def readXls(self):
		if XlsHandle.__read_book is None:
			XlsHandle.__read_book = xlrd.open_workbook(self.xls)
			self.read_sheet = XlsHandle.__read_book.sheet_by_index(0)
			XlsHandle.__xml_rows = self.read_sheet.nrows
			XlsHandle.__xml_cols = self.read_sheet.ncols

	def readXlsRCs(self):
		data = {}
		data["rows"] = XlsHandle.__xml_rows
		data["cols"] = XlsHandle.__xml_cols
		return data

	def readValue(self, rows, cols):
		value = self.read_sheet.cell(rows, cols).value
		return value

	'''------------- 给excel表中写入值 start --------------'''
	#values 插入的数据 ['t1', 't2', 't3' ... ]
	#data {"rows_add_to":"true", "cols_add_to":"true", "rows":1, "cols":1}
	def writeXls(self, values, data):
		rows = ('rows' in data.keys()) and data['rows'] or 0
		cols = ('cols' in data.keys()) and data['cols'] or 0

		#计算从第n列插入
		if (os.path.exists(self.xls)):
			self.writeOldXlsInit()
			rows = data['rows_add_to'] == 'true' and self.read_sheet.nrows or rows
			cols = data['cols_add_to'] == 'true' and self.read_sheet.ncols or cols
		else:
			self.writeNewXlsInit()
		
		#插入数据
		for value in values:
			self.write_sheet.write(rows, cols, value)
			if (data['rows_add_to'] == 'true'):
				cols += 1
			else:
				rows += 1
		self.write_book.save(self.xls)
	'''------------- 给excel表中写入值 end --------------'''

	#创建excel初始化
	def writeNewXlsInit(self):
		self.write_book = xlwt.Workbook();
		self.write_sheet = self.write_book.add_sheet(self.xls)

	#写入入老文件初始化
	def writeOldXlsInit(self):
		self.write_book = copy(XlsHandle.__read_book)
		self.write_sheet = self.write_book.get_sheet(0)


def test():
	xls = XlsHandle('b_new.xls')
	xls.writeXls(['t1', 't2', 't3'], {"rows_add_to":"false", "cols_add_to":"false", "rows":9, "cols":9})


if __name__ == '__main__':
	test()