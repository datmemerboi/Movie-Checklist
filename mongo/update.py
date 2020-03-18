from pymongo import MongoClient
from PyQt5 import QtWidgets

def UpdateIdRowFn(fromRow, toRow):
	fromID = FindIdFn(fromRow, 'Checklist')
	if(fromID):
		mongoconn = MongoClient("mongodb://localhost:27017")
		query = mongoconn.Movie.Checklist.update_one(
			{ '_id':fromID },
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

	fromID = FindIdFn(fromRow, 'Recommend')
	if(fromID):
		mongoconn = MongoClient("mongodb://localhost:27017")
		query = mongoconn.Movie.Recommend.update_one(
			{ '_id':fromID },
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