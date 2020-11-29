# Automatically backup most recent backup JSON into MongoDB in /data/
# Run directly or call AutoBackupFn()

import os
import glob

def AutoBackupFn():
	path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)) , "..", "data"))

	allFiles = glob.glob(os.path.join(path, 'Movie_Checklist_*.json'))
	if allFiles:
		latest = max(allFiles, key = os.path.getctime)
		print (latest)
	
		os.system("mongoimport --db Movie --collection Checklist --type json --file "+ latest)
	
	else:
		print("No files for now")

	allFiles = glob.glob(os.path.join(path, 'Movie_Recommend_*.json'))
	if allFiles:
		latest = max(allFiles, key = os.path.getctime)
		print (latest)
	
		os.system("mongoimport --db Movie --collection Recommend --type json --file "+ latest)
	
	else:
		print("No files for now")

if __name__ == '__main__':
	AutoBackupFn()