import shutil

#copy input from GitHub to C: local
inFile = 'Z:/GitHub/doe/tasks/201610_mapping/data/input/from_doe/y2017_pre_k_directory_map_data.csv'
inFile = 'Y:/GitHub/doe/tasks/201610_mapping/data/input/from_doe/y2017_pre_k_directory_map_data.csv'
ouFile = wi+'from_doe/y2017_pre_k_directory_map_data.csv'

shutil.copy2(inFile, ouFile)