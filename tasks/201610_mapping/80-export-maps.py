import arcpy
import glob

mxdDir = 'C:/GIS/projects/doe/tasks/201610_mapping/data/input/from_doe/20161013/Maps/2016 Pre-K Directory Maps/Maps/'
mxdDir = 'C:/GIS/RFS/44136_PREK_Directory_Maps/Maps/'
outDir = 'C:/GIS/projects/doe/tasks/201610_mapping/data/output/maps/'
#rfsDir = 'C:/GIS/RFS/44136_PREK_Directory_Maps/Maps/Repaired/'
mxdFiles = glob.glob(mxdDir+'*.mxd')

for i in mxdFiles:
	print i
	#ouMXD = i.split('/',12)[12]
	ouMXD = i.split('/',4)[4]
	ouMXD = ouMXD[5:]
	ouPDF = ouMXD.replace('.mxd','.pdf')
	print ouPDF, ouMXD
	mxd = arcpy.mapping.MapDocument(i)
	arcpy.mapping.ExportToPDF(mxd, outDir+ouPDF,convert_markers=True)

#WITH COPY TO DROPBOX BELOW

import shutil, errno

def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

incopy = 'C:/GIS/projects/doe/tasks/201610_mapping'
outcopy = 'Z:/Dropbox/Projects/doe/tasks/201610_mapping'
theFolderPath = outcopy

print 'try to erase a folder'
try:
	shutil.rmtree(theFolderPath)
except:
	print 'the folder was already missing'

copyanything(incopy, outcopy)