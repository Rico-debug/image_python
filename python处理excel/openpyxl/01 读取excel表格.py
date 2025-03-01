import openpyxl

wb = openpyxl.load_workbook('example.xlsx')

# Getting sheets from the workbook

# print(wb.sheetnames)
#
# for sheet in wb:
# 	print(sheet.title)
#
# mySheet = wb.create_sheet('mySheet')
# print(wb.sheetnames)

# sheet3 = wb.get_sheet_by_name('Sheet3')
# sheet4 = wb['mySheet']

# Getting cells from the sheets
ws = wb.active
# print(ws)
# print(ws['A1'])
# print(ws['A1'].value)

# c = ws['B1']
# print('Row {}, Column {} is {}'.format(c.row, c.column, c.value))
# print('Cell {} is {}\n'.format(c.coordinate, c.value))
#
# print(ws.cell(row=1, column=2))
# print(ws.cell(row=1, column=2).value)
# for i in range(1hcgghjjrxb, 8, 2):
# 	print(i, ws.cell(row=i, column=2).value)

# Getting rows and columns from the sheets
# colC = ws['C']
# row6 = ws[6]
# col_range = ws['B:C']
# row_range = ws[2:6]

# for col in col_range:
# 	for cell in col:
# 		print(cell.value)
#
# for row in row_range:
# 	for cell in row:
# 		print(cell.value)

# for row in ws.iter_rows(min_row=1, max_row=2, max_col=2):
# 	for cell in row:
# 		print(cell)

# print(tuple(ws.rows))
# cell_range = ws['A1:C3']
#
# for rowOfCellObjects in cell_range:
# 	for cellObj in rowOfCellObjects:
# 		print(cellObj.coordinate, cellObj.value)
# 	print('------End of Row----------')

# print('{} * {}'.format(ws.max_row, ws.max_column))

from openpyxl.utils import get_column_letter, column_index_from_string
print(get_column_letter(2), get_column_letter(47), get_column_letter(900))
print(column_index_from_string('AAH'))






# readCensusExcel.py - Tabulates population and number of census tracts
# for each county.

import openpyxl, pprint

# Read the spreadsheet data
print('Opening workbook')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.active

countryData = {}

# Fill in countryData with each city's pop and tracts
for row in range(2, sheet.max_row+1):

	# Each row in the spreasheet has data
	state = sheet['B' + str(row)].value
	country = sheet['C' + str(row)].value
	pop = sheet['D' + str(row)].value

	# make sure the key state exists
	countryData.setdefault(state, {})
	# make sure the key for country in state exists
	countryData[state].setdefault(country,{'tracts':0, 'pop':0})
	# Each row represents one census tract, so increment by one
	countryData[state][country]['tracts'] += 1
	# Increase the country pop by the pop in this census tract
	countryData[state][country]['pop'] += int(pop)

# Open a new text file and write the contents fo countryData to it
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countryData))