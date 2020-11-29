'''
To backup data from Firebase Realtime db
FileName(Collection) will return the filename for the Collection
GetFirebase(Collection) will get all records from Collection
FBbackupNowFn(Collection) will use above fns to create a JSON backup file

Firebase app from ..Firebase.cred.py
'''
import os
import sys
import json
from datetime import datetime

sys.path.append('..')
from FireBase.cred import firebase

def FileName(Collection):
	now = datetime.now().strftime("%d-%m-%Y")
	filename = "Movie"+"_"+ Collection +"_"+ now +".json"
	pathfile = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", filename))

	return pathfile

def GetFirebase(Collection):
	print("Getting", Collection)
	result = firebase.get(Collection+'/', None)
	return list(result.keys()), list(result.values())

def FBbackupNowFn(Collection):
	ids, records = GetFirebase(Collection)
	pathfile = FileName(Collection)
	File = open(pathfile, 'w')
	for index in range(len(records)):
		row = {
			'_id' : ids[index],
			'Title' : records[index]['Title'],
			'Director' : records[index]['Director'],
			'Year' : records[index]['Year'],
			'Language' : records[index]['Language']	
		}
		if 'Remarks' in records[index].keys():
			row['Remarks'] = records[index]['Remarks']

		json.dump(row, File, indent = 4, ensure_ascii = False)
		File.write('\n')
	File.close()

if __name__ == '__main__':
	FBbackupNowFn('Checklist')
	FBbackupNowFn('Recommend')