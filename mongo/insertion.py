def CheckExistingFn(self):
	mongoconn = MongoClient("mongodb://localhost:27017")
	query = mongoconn.Movie.Checklist.find({"Title":self.title.text().strip()})
	for i in query:
		if(i['Title'] == self.title.text().strip() and i["Director"] == self.director.text().strip()):
			ExistingMessage = QtWidgets.QMessageBox()
			ExistingMessage.setText("Already in List")
			ExistingMessage.setWindowTitle("Done!")
			ExistingMessage.exec_()
			return(True)
	mongoconn.close()

def InsertCheckedFn(self):
	if(not(self.CheckExistingFn())):
		if(self.title.text().strip()=='' or self.director.text().strip()=='' or self.year.text().strip()==''):
			NullMessage = QtWidgets.QMessageBox()
			NullMessage.setText("Missing few values")
			NullMessage.setWindowTitle("Error!")
			NullMessage.exec_()
		else:
			row = {"Title":self.title.text().strip(), "Director":self.director.text().strip(), "Year":self.year.text().strip(), "Language":self.language.currentText()};
			if(self.remarks.toPlainText().strip()!=''):
				row["Remarks"] = self.remarks.toPlainText().strip()
			mongoconn = MongoClient("mongodb://localhost:27017")
			query = mongoconn.Movie.Checklist.update(row, row, upsert = True)
			CheckedMessage = QtWidgets.QMessageBox()
			CheckedMessage.setText("Added to checklist")
			CheckedMessage.setWindowTitle("Done!")
			CheckedMessage.exec_()
			if(recommendBool):
				query = mongoconn.Movie.Recommend.update(row, row, upsert=True)
			mongoconn.close()
