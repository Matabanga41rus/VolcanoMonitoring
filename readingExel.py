import xlrd
from app.models import Volcano, SeismicObservation, SeismicEventType, Observation

pathExcel = 'C:/Users/Denis/Desktop/excel_python/26_Dlz.xlsx'

rb = xlrd.open_workbook(pathExcel)
sheet = rb.sheet_by_index(0)

dates = sheet.col_values(2)
dates.remove('')
times = sheet.col_values(3)
times.remove('')
station = sheet.col_values(4)
station.remove('')





