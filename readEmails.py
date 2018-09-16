import xlrd
import os
import sys

#loc = '/test.xlxs'

dir = os.path.dirname(__file__)
loc = os.path.join(dir, 'test.xlsx')

#open workbook

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# open/create text file
file = open("email.txt", "w+")

numRows = sheet.nrows

#For row 0 and column 0
i = 0
while i < numRows:
	val = sheet.cell_value(i, 0)
	if len(val) == 0:
		break
	file.write(val + "@scarletmail.rutgers.edu\n")
	i = i + 1
file.close()

