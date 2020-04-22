# Push chosen collection to Firebase Realtime Database
# Application works on cmd line interface only
# Firebase app from Firebase.cred.py
import os
from pymongo import MongoClient
from FireBase.cred import firebase

def __main__():
	coll = input("Choose Collection (C/R) or Q to quit: ").upper()
	
	if(coll=="C"):
		print("Checklist will be posted")

		mongoconn = MongoClient("mongodb://localhost:27017")
		query = mongoconn.Movie.Checklist.find()

		for row in query:
			del row['_id']
			if('Remarks' in row.keys() and row['Remarks']==""):
				del row['Remarks']
			firebase.post('Checklist/', row)

	elif(coll=="R"):
		print("Recommend will be posted")

		mongoconn = MongoClient("mongodb://localhost:27017")
		query = mongoconn.Movie.Recommend.find()

		for row in query:
			del row['_id']
			if('Remarks' in row.keys() and row['Remarks']==""):
				del row['Remarks']
			firebase.post('Recommend/', row)

	elif(coll=="Q"):
		print("Bye.")
		exit()
	
	else:
		print("--- Try again ---")
		__main__()
__main__()