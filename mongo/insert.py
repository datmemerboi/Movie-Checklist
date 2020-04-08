# Insert a row into MongoDB
'''
CheckExistingFn(row) checks presence of Title & Director combo in MongoDB
InsertCheckedFn(Row, recommendBool):
-	checks existing or not
-	inserts row into MongoDB checklist
-	inserts row into MongoDB Recommend list based on recommendBool (True / False)
'''

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
		ChecklistMessage = QtWidgets.QMessageBox()
		ChecklistMessage.setText("Added to checklist")
		ChecklistMessage.setWindowTitle("Done!")
		ChecklistMessage.exec_()
		if(recommendBool):
			query = mongoconn.Movie.Recommend.update(row, row, upsert=True)
			RecommendMessage = QtWidgets.QMessageBox()
			RecommendMessage.setText("Added to Recommended")
			RecommendMessage.setWindowTitle("Done!")
			RecommendMessage.exec_()
		mongoconn.close()
