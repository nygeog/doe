import arcpy
import glob

mxdDir = 'C:/GIS/projects/doe/tasks/201610_mapping/data/input/from_doe/20161013/Maps/2016 Pre-K Directory Maps/Maps/'
outDir = 'C:/GIS/projects/doe/tasks/201610_mapping/data/output/maps/'
mxdFiles = glob.glob(mxdDir+'*.mxd')

for i in mxdFiles:
	print i
	ouPDF = i.split('/',12)[12]
	ouPDF = ouPDF[5:]
	ouPDF = ouPDF.replace('.mxd','.pdf')
	print ouPDF
	mxd = arcpy.mapping.MapDocument(i)
	arcpy.mapping.ExportToPDF(mxd, outDir+ouPDF,convert_markers=True)