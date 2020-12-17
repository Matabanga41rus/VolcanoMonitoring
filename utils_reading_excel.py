import xlrd
from xlrd import xldate_as_datetime

class Utils:
    def translateDate(excelDate):
        return xldate_as_datetime(float(excelDate), 0).strftime('%d.%m.%Y')

    def translateTime(excelTime):
        return xldate_as_datetime(float(excelTime), 0).strftime('%H:%M:%S')