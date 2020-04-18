# Push data to Firbase Realtime Database
'''
PushToFirebase() requires:
-	Row to be pushed to Checklist/
-	bool variable True: Push to Recommend/, False: Not to
'''

from firebase import firebase
from PyQt5 import QtWidgets

firebase = firebase.FirebaseApplication("", authentication=None)

def PushToFirebase(row, recommendBool):
	checklistResult = firebase.post('Checklist/', row)
	if recommendBool :
		recommendResult = firebase.post('Recommend/', row)
	if checklistResult :
		CheckedMessage = QtWidgets.QMessageBox()
		CheckedMessage.setText("Added to Firebase checlist")
		CheckedMessage.setWindowTitle("Done!")
		CheckedMessage.exec_()
	if recommendResult :
		CheckedMessage = QtWidgets.QMessageBox()
		CheckedMessage.setText("Added to Firebase Recommended")
		CheckedMessage.setWindowTitle("Done!")
		CheckedMessage.exec_()