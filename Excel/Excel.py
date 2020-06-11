# coding = utf-8

import xlrd
'''

#打开文件
data = xlrd.open_workbook('/Users/app005synergy/Desktop/ios用户评论汇总0225.xlsx')

#查看工作表
sheetNames = data.sheet_names()
print("sheets : " + str(sheetNames))

#通过文件名获取工作表，获取 Sheet1
table = data.sheet_by_name('Sheet1')
# 或者使用第一个表
# table = data.sheet_by_index(0)

#获取行数和列数
# 行 table.nrows
# 列 table.ncols
print("总行数 ：" + str(table.nrows))
print("总列数 ：" + str(table.ncols))

# 获取整行的值和整列的值
# 整行值
rowValues = table.row_values(0)
# 整列值
colValues = table.col_values(1)

print('整行值' + str(rowValues))
print('整列值' + str(colValues))
# 获取某一个单元格的值
cel_B2 = table.cell(1,1).value
print("第2行B列的值" + cel_B2)
'''

def read_xlrd(excelFIle):
    # 打开文件
    data = xlrd.open_workbook(excelFIle)
    # 取出第一个表
    table = data.sheet_by_index(0)

    for rowNum in range(table.nrows):
        # 读取行的值
        rowValue = table.row_values(rowNum)
        for colNum in range(table.ncols):
            print(rowValue[colNum])

        print("---------")


if __name__ == '__main__':
    read_xlrd("/Users/app005synergy/Desktop/ios用户评论汇总0225.xlsx")