import os
from datetime import datetime

def BackupNowFn(database, collection):
	now = datetime.now().strftime("_%d-%b-%y_%H:%M:%S")
	query = "mongoexport --db "+database+" --collection "+collection+" --out "+os.path.realpath(os.getcwd())+"/backup/"+database+collection+now+".json"
	os.system(query)