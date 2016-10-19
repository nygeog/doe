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