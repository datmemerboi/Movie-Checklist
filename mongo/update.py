from pymongo import MongoClient
from PyQt5 import QtWidgets

def SearchRowFn(window, row):
	print("entered Search row")
	mongoconn = MongoClient("mongodb://localhost:27017")
	query = mongoconn.Movie.Checklist.find({
		'$and':[
			{ "Title": {'$regex' : str(row['Title']), '$options' : 'i'} },
			{ "Director":{'$regex' : str(row['Director']), '$options':'i'} }
		]
		})
	print(row)
	for element in query:
		print(element)
		MakeSure = QtWidgets.QMessageBox()
		res = MakeSure.question(self, '', 
			"Do you want to update: "+
			element['Title']+" by "+element['Director']+
			"to\n"+row['Title']+" by "+row['Director']+" ?",
			MakeSure.Yes | MakeSure.No)
		# MakeSure.setText("Missing few values")
		MakeSure.setWindowTitle("Making sure..")
		MakeSure.exec_()
	mongoconn.close()