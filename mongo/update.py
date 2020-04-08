# To update existing row in MongoDB
# FindIdFn(Row, Collection) returns ID of Row in a Collection
# UpdateIdRowFn(from, to) updates from based on ID

from pymongo import MongoClient
from PyQt5 import QtWidgets

def FindIdFn(fromRow, Collection):
	mongoconn = MongoClient("mongodb://localhost:27017")
	query = mongoconn.Movie[Collection].find({
		'$and':[
			{ "Title": {'$regex' : str(fromRow['Title']), '$options' : 'i'} },
			{ "Director":{'$regex' : str(fromRow['Director']), '$options':'i'} }
		]
		})
	mongoconn.close()
	for res in query:
		return res['_id']

def UpdateIdRowFn(fromRow, toRow):
	checklistID = FindIdFn(fromRow, 'Checklist')
	if(checklistID):
		mongoconn = MongoClient("mongodb://localhost:27017")
		if("Remarks" in fromRow.keys() and "Remarks" not in toRow.keys()):
			mongoconn.Movie.Checklist.update(
				{ '_id':checklistID },
				{ '$unset': { 'Remarks':1 } }
				);
		query = mongoconn.Movie.Checklist.update_one(
			{ '_id':checklistID },
			{ '$set':toRow }
			);
		mongoconn.close()
		if(query):
			UpdateMessage = QtWidgets.QMessageBox()
			UpdateMessage.setText("Updated in Checklist")
			UpdateMessage.setWindowTitle("Updated")
			UpdateMessage.exec_()
		else:
			ErrorMessage = QtWidgets.QMessageBox()
			ErrorMessage.setText("Couldn't update :(")
			ErrorMessage.setWindowTitle("Error!")
			ErrorMessage.exec_()

	recommmendID = FindIdFn(fromRow, 'Recommend')
	if(recommmendID):
		mongoconn = MongoClient("mongodb://localhost:27017")
		if("Remarks" in fromRow.keys() and "Remarks" not in toRow.keys()):
			mongoconn.Movie.Recommend.update(
				{ '_id':recommmendID },
				{ '$unset': { 'Remarks':1 } }
				);
		query = mongoconn.Movie.Recommend.update_one(
			{ '_id':recommmendID },
			{ '$set':toRow }
			);
		mongoconn.close()
		if(query):
			UpdateMessage = QtWidgets.QMessageBox()
			UpdateMessage.setText("Updated in Recommend")
			UpdateMessage.setWindowTitle("Updated")
			UpdateMessage.exec_()
		else:
			ErrorMessage = QtWidgets.QMessageBox()
			ErrorMessage.setText("Couldn't update :(")
			ErrorMessage.setWindowTitle("Error!")
			ErrorMessage.exec_()