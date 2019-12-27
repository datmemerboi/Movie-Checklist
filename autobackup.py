# Automatically importing most recent backup into Mongodb
import os, re; from datetime import datetime
thisyear = datetime.now().strftime("%y");thismonth = datetime.now().strftime("%m");thisday = datetime.now().strftime("%d")

foundit = False

def recentDateFn():
	for name in os.listdir("backup"):
		match = re.findall("Recommend"+"_"+thisday+"-"+thismonth+"-"+thisyear+"_[0-9]+:[0-9]+.json$", name)
		if(match):
			print(name+" is most recent")
			foundit = True
			# os.system("mongoimport --db "+database+" --collection "+collection+" --type json --file backup/"+name)
			break

if(not(foundit)):
	thisday = str(int(thisday)-1)
	recentDateFn()