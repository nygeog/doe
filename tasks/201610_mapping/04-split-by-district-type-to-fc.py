import arcpy

inGDB = 'C:/GIS/projects/doe/tasks/201610_mapping/data/input/from_doe/y2017_pre_k_directory_map_data.gdb/'
ouGDB = 'C:/GIS/RFS/44136_PREK_Directory_Maps/Data/PREK_Directory_Data.gdb/'

districts = range(32)
types =  ['Charter School','District School','NYCEEC','Pre-K Center']
typesN = ['Charter_District','Pub_District','EEC_District','Centers_District'] #These have been validated District Shool <-> Pub_District; Pre-K Center <-> Centers_District

for i in districts:
	i = i+1
	iz = str(i)
	if len(iz) == 1:
		iz = '0'+iz
	arcpy.Select_analysis(in_features=inGDB+"y2017_pre_k_directory_map_data_xy", out_feature_class=ouGDB+'D'+iz, where_clause="District = "+str(i))
	for j, k in zip(types,typesN):
		print j, iz
		print k, iz
		arcpy.Select_analysis(in_features=inGDB+"y2017_pre_k_directory_map_data_xy", out_feature_class=ouGDB+k+iz, where_clause="District = "+str(i)+" AND type = '"+j+"'")
		# if k == 'Charter_District':
		# 	arcpy.CalculateField_management(in_table=ouGDB+k+iz, field="ADMIN_DIST", expression="84", expression_type="PYTHON", code_block="")
