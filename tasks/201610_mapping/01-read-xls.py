import pandas as pd

xlsFile = '/Users/danielmsheehan/Desktop/Maps/2017 Pre-K Directory Map Data DRAFT.xlsx'

df = pd.io.excel.read_excel(xlsFile, 'Sheet1')

print df.head(10)

ouCSV = '/Users/danielmsheehan/Desktop/Maps/y2017_pre_k_directory_map_data_draft.csv'

df.to_csv(ouCSV, index=False, encoding='utf-8')