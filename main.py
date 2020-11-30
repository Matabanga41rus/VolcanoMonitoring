import xlrd
print('dfsdfs')





pathExcel = 'C:/Users/Denis/Desktop/excel_python/26_Dlz.xlsx'



def getDataExcel(pathExcel):
    rb = xlrd.open_workbook(pathExcel)
    sheet = rb.sheet_by_index(0)

    date = sheet.col_values(2)
    time = sheet.col_values(3)
    station = sheet.col_values(4)
    volcano = sheet.col_values(6)
    countEvent = sheet.col_values(8)

    return 0
