import xlrd


pathExcel = './26_Dlz.xlsx'

rb = xlrd.open_workbook(pathExcel)
sheet = rb.sheet_by_index(0)

dates = sheet.col_values(2)
dates.remove('')
times = sheet.col_values(3)
times.remove('')
station = sheet.col_values(4)
station.remove('')
volcanoes = sheet.col_values(5)
typeEvents = sheet.col_values(6)
countEvents = sheet.col_values(7)
duration = sheet.col_values(8)










