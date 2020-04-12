# Update data on Firebase Realtime Database
'''
FindFirebaseIdFn(Row, Collection) to find the ID of mentioned Row in firebase/Collection/
CompareFromToFn(from, to) to compare and filter only necessary key,value pairs
PutFirebaseIdRowFn(from, to) used aforementioned fns to update from into to
'''

from firebase import firebase
firebase = firebase.FirebaseApplication("", authentication=None)
from PyQt5 import QtWidgets

def FindFirebaseIdFn(fromRow, Collection):
	findRes = firebase.get(str(Collection), None)
	for index in range(len(findRes)):
		if( list(findRes.values())[index]['Title']==fromRow['Title'] and
			list(findRes.values())[index]['Director']==fromRow['Director']
		 ):
			return list(findRes.keys())[index]
	return

def CompareFromToFn(fromRow, toRow):
	if(fromRow['Title']==toRow['Title']):
		toRow.pop('Title', None)
	if(fromRow['Director']==toRow['Director']):
		toRow.pop('Director', None)
	if(fromRow['Year']==toRow['Year']):
		toRow.pop('Year', None)
	if(fromRow['Language']==toRow['Language']):
		toRow.pop('Language', None)
	if('Remarks' in fromRow.keys() and 'Remarks' in toRow.keys() and fromRow['Remarks']==toRow['Remarks'] ):
		toRow.pop('Remarks', None)
	return toRow

def PutFirebaseIdRowFn(fromRow, toRow):
	newToRow = CompareFromToFn(fromRow, toRow)
	
	checklistID = FindFirebaseIdFn(fromRow, "Checklist/"); recommendID = FindFirebaseIdFn(fromRow, "Recommend/")

	if('Remarks' in fromRow.keys() and 'Remarks' not in toRow):
		firebase.delete('Checklist/'+checklistID+"/Remarks", None)
		firebase.delete('Recommend/'+recommendID+"/Remarks", None)
	
	for eachKey in newToRow:
		if(checklistID):
			if( firebase.put( 'Checklist/'+checklistID,eachKey, newToRow[eachKey] ) ):
				UpdateMessage = QtWidgets.QMessageBox()
				UpdateMessage.setText("Updated checklist")
				UpdateMessage.setWindowTitle("Updated!")
				UpdateMessage.exec_()
			else:
				ErrorMessage = QtWidgets.QMessageBox()
				ErrorMessage.setText("An error occured")
				ErrorMessage.setWindowTitle("Error!")
				ErrorMessage.exec_()

		if(recommendID):
			if( firebase.put( 'Recommend/'+recommendID,eachKey, newToRow[eachKey] ) ):
				UpdateMessage = QtWidgets.QMessageBox()
				UpdateMessage.setText("Updated recommened")
				UpdateMessage.setWindowTitle("Updated!")
				UpdateMessage.exec_()
			else:
				ErrorMessage = QtWidgets.QMessageBox()
				ErrorMessage.setText("An error occured")
				ErrorMessage.setWindowTitle("Error!")
				ErrorMessage.exec_()