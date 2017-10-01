import xlrd
workbook=xlrd.open_workbook('F:\\冶金144班\\冶金144班2016-2017上学年奖项工作.xlsx')
worksheets=workbook.sheet_names()
print('worksheets is %s'%worksheets)
worksheet1=workbook.sheet_by_name('Sheet1')
num_rows=worksheet1.nrows
for curr_row in range(num_rows):
    row=worksheet1.row_values(curr_row)
    print('row%s is %s'%(curr_row,row))
num_cols = worksheet1.ncols
for curr_col in range(num_cols):
    col = worksheet1.col_values(curr_col)
    print('col%s is %s' %(curr_col,col))
for rown in range(num_rows):
    for coln in range(num_cols):
        cell = worksheet1.cell_value(rown,coln)
        print(cell)
