import arcpy
import glob

mxdDir = 'C:/GIS/projects/doe/tasks/201610_mapping/data/input/from_doe/20161013/Maps/2016 Pre-K Directory Maps/Maps/'
outDir = 'C:/GIS/projects/doe/tasks/201610_mapping/data/output/maps/'
rfsDir = 'C:/GIS/RFS/44136_PREK_Directory_Maps/Maps/Repaired/'
mxdFiles = glob.glob(mxdDir+'*.mxd')

for i in mxdFiles:
	print i
	ouMXD = i.split('/',12)[12]
	ouMXD = ouMXD[5:]
	ouPDF = ouMXD.replace('.mxd','.pdf')
	print ouPDF, ouMXD
	mxd = arcpy.mapping.MapDocument(i)
	mxd.findAndReplaceWorkspacePaths('C:/Users/jhall/Documents/ArcGIS/Packages/SubwayStations_Master/commondata/data0','C:/GIS/MTA')
	
	print rfsDir+ouMXD
	mxd.saveACopy(mxdDir+'Repaired/'+ouMXD)
	mxd = arcpy.mapping.MapDocument(rfsDir+ouMXD)
	arcpy.mapping.ExportToPDF(mxd, outDir+ouPDF,convert_markers=True)