import openpyxl
data =openpyxl.load_workbook('F:\\Game\\test.xlsx')
print(type(data))
sheet=data.get_sheet_by_name('Sheet1')
print(sheet['A1'])
print(sheet['A2'].value)