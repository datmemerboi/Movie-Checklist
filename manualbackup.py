# Manually importing backup JSON into Mongodb
# Run file as: python3 manualbackup.py backup/fileToBackUp_Date_Time.JSON

import sys, os
if __name__=="__main__":
	pathfile = sys.argv[1] 
	sys.argv[1] = sys.argv[1].replace("backup/", '')
	print(sys.argv[1])
	spl = sys.argv[1].strip('.json').split('_')
	database = spl[0];collection = spl[1]
	os.system("mongoimport --db "+database+" --collection "+collection+" --type json --file "+pathfile)