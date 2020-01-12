import os
from datetime import datetime

def BackupNowFn(database, collection):
	now = datetime.now().strftime("%d-%m-%Y")
	filename = database+"_"+collection+"_"+now
	query = "mongoexport --db "+database+" --collection "+collection+" --out "+os.path.realpath(os.getcwd())+"/backup/"+filename+".json"
	os.system(query)