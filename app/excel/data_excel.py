import pyexcel as ex
import pylightxl as pl

wb1 = ex.get_array(file_name ='26_Dlz.xlsx')


wb2 = pl.readxl(fn='26_Dlz.xlsx')
for col in wb2.ws('26_Dlz').rows:
    print(col[3])
    if col[6] == '':
        break










