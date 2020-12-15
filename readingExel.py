import xlrd
from utilsReadingExcel import Utils


pathExcel = './26_Dlz.xlsx'
indexNameCol = 0

rb = xlrd.open_workbook(pathExcel)
sheet = rb.sheet_by_index(0)

dates = sheet.col_values(2)
dates.remove('')

times = sheet.col_values(3)
times.remove('')

station = sheet.col_values(4)
station.remove('')

volcanoes = sheet.col_values(6)
volcanoes.remove(volcanoes[indexNameCol])

typeEvents = sheet.col_values(7)
typeEvents.remove(typeEvents[indexNameCol])

countEvents = sheet.col_values(8)
countEvents.remove(countEvents[indexNameCol])

duration = sheet.col_values(9)
duration.remove(duration[indexNameCol])

CirAt = sheet.col_values(10)
CirAt.remove(CirAt[indexNameCol])

CirAtMax = sheet.col_values(11)
CirAtMax.remove(CirAtMax[indexNameCol])

CirClass = sheet.col_values(12)
CirClass.remove(CirClass[indexNameCol])

for index in range(sheet.nrows-1):
    print(Utils.translateTime(times[index]), volcanoes[index], station[index], CirAtMax[index])










