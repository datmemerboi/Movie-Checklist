from pymongo import MongoClient
from PyQt5 import QtWidgets

def CheckExistingFn(row):
	mongoconn = MongoClient("mongodb://localhost:27017")
	query = mongoconn.Movie.Checklist.find({"Title":row['Title']})
	for i in query:
		if(i['Title'] == row['Title'] and i["Director"] == row['Director']):
			ExistingMessage = QtWidgets.QMessageBox()
			ExistingMessage.setText("Already in List")
			ExistingMessage.setWindowTitle("Done!")
			ExistingMessage.exec_()
			return(True)
	mongoconn.close()

def InsertCheckedFn(row, recommendBool):
	if(not(CheckExistingFn(row))):
		mongoconn = MongoClient("mongodb://localhost:27017")
		query = mongoconn.Movie.Checklist.update(row, row, upsert = True)
		CheckedMessage = QtWidgets.QMessageBox()
		CheckedMessage.setText("Added to checklist")
		CheckedMessage.setWindowTitle("Done!")
		CheckedMessage.exec_()
		if(recommendBool):
			query = mongoconn.Movie.Recommend.update(row, row, upsert=True)
		mongoconn.close()
