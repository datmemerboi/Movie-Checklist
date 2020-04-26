# Update data on Firebase Realtime Database
'''
Firebase ID obtained from cred.py
FbaseFromRowFn(from, Collection) will find the actual row in Firebase db
EliminateKeys(from, to) remove the same values in ToRow
PutFbaseRowFn(from, to) used aforementioned fns to update from into to
'''

from .cred import firebase
from PyQt5 import QtWidgets

def FbaseFromRowFn(mongoFrom, Collection):
	findRes = firebase.get( Collection, None)
	for index in range( len(findRes) ):
		if( list(findRes.values())[index]['Title']==mongoFrom['Title'] and
			list(findRes.values())[index]['Director']==mongoFrom['Director'] ):
			return list(findRes.keys())[index] , list(findRes.values())[index]
	return False

def EliminateKeys(From, To):
	if(From['Title']==To['Title']):
		To.pop('Title', None)
	
	if(From['Director']==To['Director']):
		To.pop('Director', None)
	
	if(From['Year']==To['Year']):
		To.pop('Year', None)
	
	if(From['Language']==To['Language']):
		To.pop('Language', None)
	
	if('Remarks' in From.keys() and 'Remarks' in To.keys() and From['Remarks']==To['Remarks'] ):
		To.pop('Remarks', None)

	return To

def PutFbaseRowFn(mongoFrom, toRow):
	checklistID, checklistRow = FbaseFromRowFn( mongoFrom, 'Checklist')
	recommendID, recommenedRow = FbaseFromRowFn( mongoFrom, 'Recommend')

	checklistRow = EliminateKeys(dict(checklistRow), dict(toRow))
	recommenedRow = EliminateKeys(dict(recommenedRow), dict(toRow))
	
	if checklistID:
		if('Remarks' in mongoFrom.keys() and 'Remarks' not in checklistRow.keys() ):
			firebase.delete('Checklist/'+checklistID+"/Remarks", None)
		
		for each in checklistRow.keys():
			if( firebase.put( 'Checklist/'+checklistID, each, checklistRow[each] ) ):
				UpdateMessage = QtWidgets.QMessageBox()
				UpdateMessage.setText("Updated checklist")
				UpdateMessage.setWindowTitle("Updated!")
				UpdateMessage.exec_()
			else:
				ErrorMessage = QtWidgets.QMessageBox()
				ErrorMessage.setText("An error occured")
				ErrorMessage.setWindowTitle("Error!")
				ErrorMessage.exec_()

	if recommendID:
		if('Remarks' in mongoFrom.keys() and 'Remarks' not in recommenedRow.keys() ):
			firebase.delete('Recommend/'+recommendID+"/Remarks", None)
		
		for each in recommenedRow.keys():
			if( firebase.put( 'Recommend/'+recommendID, each, recommenedRow[each] ) ):
				UpdateMessage = QtWidgets.QMessageBox()
				UpdateMessage.setText("Updated recommened")
				UpdateMessage.setWindowTitle("Updated!")
				UpdateMessage.exec_()
			else:
				ErrorMessage = QtWidgets.QMessageBox()
				ErrorMessage.setText("An error occured")
				ErrorMessage.setWindowTitle("Error!")
				ErrorMessage.exec_()