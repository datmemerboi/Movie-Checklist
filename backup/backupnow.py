# Create backup file of specified database & collection in /data/
# Run directly or call BackupNowFn(db, coll) with arguments

import os
from datetime import datetime

def BackupNowFn(database, collection):
	now = datetime.now().strftime("%d-%m-%Y")
	filename = database+"_"+collection+"_"+now
	
	path = os.path.join( os.path.dirname(os.path.realpath(__file__)), "../data/")

	query = "mongoexport --db "+database+" --collection "+collection+" --out "+path+filename+".json"
	
	os.system(query)

if __name__ == '__main__':
	BackupNowFn('Movie', 'Checklist')
	BackupNowFn('Movie', 'Recommend')