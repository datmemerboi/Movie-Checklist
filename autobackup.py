# Automatically backup most recent backup JSON into MongoDB

import glob, os

allFiles = glob.glob('backup/Movie_Checklist_*.json')
if(allFiles):
	latest = max(allFiles, key = os.path.getctime)
	print (latest)
	os.system("mongoimport --db Movie --collection Checklist --type json --file "+latest)
else:
	print("No files for now")

allFiles = glob.glob('backup/Movie_Recommend_*.json')
if(allFiles):
	latest = max(allFiles, key = os.path.getctime)
	print (latest)
	os.system("mongoimport --db Movie --collection Recommend --type json --file "+latest)
else:
	print("No files for now")