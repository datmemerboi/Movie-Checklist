# Manually importing backup into Mongodb
# Run file as such: python3 manualbackup.py backup/filetobebackedup_date_time.json

import sys, os
if __name__=="__main__":
	pathfile = sys.argv[1] 
	sys.argv[1] = sys.argv[1].replace("backup/", '')
	print(sys.argv[1])
	spl = sys.argv[1].strip('.json').split('_')
	database = spl[0];collection = spl[1]
	os.system("mongoimport --db "+database+" --collection "+collection+" --type json --file "+pathfile)