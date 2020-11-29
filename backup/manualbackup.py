# Manually importing backup JSON into Mongodb
# Mention file to be backed up as an argument

import sys, os, re

def main():
	if("data/" in sys.argv[1]):
		sys.argv[1] = re.sub(r".*data/", "", sys.argv[1])
	
	filename = sys.argv[1]
	print(filename, " will be used for backup")
	
	path = os.path.join( os.path.dirname(os.path.realpath(__file__)), "../data/")

	spl = sys.argv[1].strip('.json').split('_')
	database = spl[0]; collection = spl[1]
	
	os.system("mongoimport --db "+ database +" --collection "+ collection +" --type json --file "+ path + filename)

if __name__=="__main__":
	main()