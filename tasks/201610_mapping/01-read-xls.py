import pandas as pd
from _settings_mac import *

xlsFile = wi+'/from_doe/20161014/2017 Pre-K Directory Map Data FINAL.xlsx' #n = 1820

df = pd.io.excel.read_excel(xlsFile, 'Sheet1')

df = df.rename(columns=lambda x: x.replace('Address','address').replace('ZIP','zip'))

df['LocCode'] = 'test'
df['LocName'] = df['Name']
df['phone'] = 'missing'
df['income'] = 'N'
df['Day_Length'] = 1
df['SPCoordX'] = df['X_Coord_GBAT']
df['SPCoordY'] = df['Y_Coord_GBAT']
df['PjAreaName'] = 'missing'
df['BORONUM'] = 0
df['BIN'] = 0
df['BBL'] = ''
df['DCH_DC_ID'] = ''
df['Seats'] = 1
df['Contract'] = ''
df['InitDate'] = '12/1/2000'
df['TotalViol'] = 1
df['Inspected'] = '12/1/2000'
df['DOHPermit'] = '12/1/2000'
df['POINT_X'] = 1
df['POINT_Y'] = 1
df['WebSite'] = 'missing'
df['Email']   = 'email'
df['ORG_TAX_ID'] = ''
df['PKType'] = 'missing'
df['Meals'] = 1
df['OutdoorIndoor'] = 1
df['ExtendedDay'] = 1
df['SEMS'] = ''
df['Button_type'] = 'missing'
df['PEPApproved'] = 1
df['ADMIN_DIST'] = 1

# EEC District

# PEPApproved    Value 1 Label PEPApproved

# Centers District

# PEPApproved    Value 1 Label Pre-K Center

# Pub District

# ADMIN_DIST   Value 1 Label District School

# Charter School

# ADMIN_DIST  Value 1 Label Charter School

print df.head(10)

print len(df.index)

df = df[['SiteID','type','LocCode','Borough','District','LocName','phone','address','zip','income','Day_Length','SPCoordX','SPCoordY','PjAreaName','BORONUM','BIN','BBL','DCH_DC_ID','Seats','Contract','InitDate','TotalViol','Inspected','DOHPermit','POINT_X','POINT_Y','WebSite','Email','ORG_TAX_ID','PEPApproved','PKType','Meals','OutdoorIndoor','ExtendedDay','SEMS','Button_type','type','ADMIN_DIST']]

print df.head(10)
for i in df.columns:
	print i

ouCSV = wi+'/from_doe/y2017_pre_k_directory_map_data.csv'

df.to_csv(ouCSV, index=False, encoding='utf-8')