from pymongo import MongoClient
from PyQt5 import QtWidgets

def SearchRowFn(row):
	print("entered Search row")
	mongoconn = MongoClient("mongodb://localhost:27017")
	query = mongoconn.Movie.Checklist.find({
		'$and':[
			{ "Title": {'$regex' : str(row['Title']), '$options' : 'i'} },
			{ "Director":{'$regex' : str(row['Director']), '$options':'i'} }
		]
		})
	print(row)
	for i in query:
		print(i)
	mongoconn.close()