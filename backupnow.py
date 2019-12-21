import os
from datetime import datetime

def BackupNowFn(database, collection):
	# now = datetime.now().strftime("_%d-%b-%y_%H:%M")
	now = datetime.now().strftime("_%d-%m-%Y_%H:%M")
	filename = database+"_"+collection+now
	query = "mongoexport --db "+database+" --collection "+collection+" --out "+os.path.realpath(os.getcwd())+"/backup/"+filename+".json"
	os.system(query)