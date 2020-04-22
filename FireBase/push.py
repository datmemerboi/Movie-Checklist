# Push data to Firbase Realtime Database
'''
PushToChecklist(row) posts row in Firebase db (obtained from cred.py)
PushToRecommend(row) posts row in Firebase db (obtained from cred.py)
PushToFirebase() decides which functions to call
'''

from cred import firebase
from PyQt5 import QtWidgets

def PushToChecklist(row):
	checklistResult = firebase.post('Checklist/', row)
	if checklistResult :
		CheckedMessage = QtWidgets.QMessageBox()
		CheckedMessage.setText("Added to Firebase checlist")
		CheckedMessage.setWindowTitle("Done!")
		CheckedMessage.exec_()

def PushToRecommend(row):
	recommendResult = firebase.post('Recommend/', row)
	if recommendResult :
		CheckedMessage = QtWidgets.QMessageBox()
		CheckedMessage.setText("Added to Firebase Recommended")
		CheckedMessage.setWindowTitle("Done!")
		CheckedMessage.exec_()

def PushToFirebase(row, recommendBool):
	PushToChecklist(row)
	if recommendBool :
		PushToRecommend(row)
		