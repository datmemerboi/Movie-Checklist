import os, re; from datetime import datetime
thisyear = datetime.now().strftime("%Y")
thismonth = datetime.now().strftime("%m")
thisday = datetime.now().strftime("%d")
print(thisyear, thismonth, thisday)

foundit = False

def findYear(argument):
	global thisyear
	if(re.findall(".*"+thisyear+".json", argument)):
		return True

def findMonth(argument):
	global thismonth
	if(re.findall(".*"+thismonth+"-[0-9]{4}.json", argument)):
		return True

def findDay(argument):
	global thisday, thismonth
	if(re.findall(".*"+thisday+"-[0-9]{2}-[0-9]{4}.json", argument)):
		return True

for name in os.listdir("backup"):
	YearRet = findYear(name)
	MonthRet = findMonth(name)
	DayRet = findDay(name)
	if(YearRet and MonthRet and DayRet):
		print(name+" is it")
