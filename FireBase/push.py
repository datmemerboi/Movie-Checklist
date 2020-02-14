from firebase import firebase
from PyQt5 import QtWidgets

firebase = firebase.FirebaseApplication("https://movie-checklist-6969.firebaseio.com/", authentication=None)

def PushToFirebase(row, recommendBool):
	checklistResult = firebase.post('Checklist/', row)
	if(recommendBool):
		recommendResult = firebase.post('Recommend/', row)
	if(checklistResult):
		CheckedMessage = QtWidgets.QMessageBox()
		CheckedMessage.setText("Added to Firebase")
		CheckedMessage.setWindowTitle("Done!")
		CheckedMessage.exec_()