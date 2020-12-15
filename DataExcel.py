import pandas as pd

nameFile = '26_Dlz.xlsx'
pathExcel = './' + nameFile

data_pd = pd.read_excel(pathExcel, sheet_name='26_Dlz')

dates = data_pd.iloc[:,[2]]
times = data_pd.iloc[:,[3]]
station = data_pd.iloc[:,[4]]

volcano = data_pd['вулкан']











