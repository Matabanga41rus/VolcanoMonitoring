import xlrd
from xlrd import xldate_as_datetime
from utilsReadingExcel import Utils

pathExcel = 'C:/Users/Denis/Desktop/excel_python/26_Dlz.xlsx'

rb = xlrd.open_workbook(pathExcel)
sheet = rb.sheet_by_index(0)

dates = sheet.col_values(2).remove('')
times = sheet.col_values(3).remove('')
station = sheet.col_values(4).remove('')


for time in times:
    print(Utils.translateTime(time))




def getDataExcel(pathExcel):
    rb = xlrd.open_workbook(pathExcel)
    sheet = rb.sheet_by_index(0)

    date = sheet.col_values(2)
    time = sheet.col_values(3)
    station = sheet.col_values(4)
    volcano = sheet.col_values(6)
    countEvent = sheet.col_values(8)

    return 0
