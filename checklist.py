from PyQt5 import QtWidgets, QtCore
from pymongo import MongoClient
recommendBool = False

class ChecklistClass(object):
	def ChecklistFn(self, window):
		window.setWindowTitle("Movie Checklist")

		File = open("css/input.css", 'r')
		inputCSS = File.read().strip()
		File.close()

		File = open("css/button.css", 'r')
		buttonCSS = File.read().strip()
		File.close()

		PrintBtn = QtWidgets.QPushButton(window)
		PrintBtn.setStyleSheet(buttonCSS)
		PrintBtn.move(500, 0)
		PrintBtn.resize(70, 30)
		PrintBtn.setText("Print")
		PrintBtn.clicked.connect(lambda: self.PrintListFn())

		self.title = QtWidgets.QLineEdit(window)
		self.title.setStyleSheet(inputCSS)
		self.title.resize(350, 45)
		self.title.move(125, 90)
		self.title.setPlaceholderText("Title")

		self.director = QtWidgets.QLineEdit(window)
		self.director.setStyleSheet(inputCSS)
		self.director.resize(350, 45)
		self.director.move(125, 180)
		self.director.setPlaceholderText("Director")

		self.year = QtWidgets.QLineEdit(window)
		self.year.setStyleSheet(inputCSS)
		self.year.resize(100, 45)
		self.year.move(155, 270)
		self.year.setPlaceholderText("Year")

		self.language = QtWidgets.QComboBox(window)
		self.language.addItems(['English', 'Tamil', 'Malayalam', 'Others'])
		self.language.setStyleSheet(inputCSS)
		self.language.resize(120,35)
		self.language.move(325, 275)

		self.remarks = QtWidgets.QTextEdit(window)
		self.remarks.setStyleSheet(inputCSS+"padding-top:15;")
		self.remarks.setPlaceholderText("Remarks, if any..")
		self.remarks.resize(350, 150)
		self.remarks.move(125, 340)

		AddBtn = QtWidgets.QPushButton(window)
		AddBtn.setStyleSheet(buttonCSS)
		AddBtn.move(230, 525)
		AddBtn.resize(70, 30)
		AddBtn.setText("Check")
		AddBtn.clicked.connect(lambda: self.InsertCheckedFn())

		recommendBtn = QtWidgets.QCheckBox(window)
		recommendBtn.setChecked(False)
		recommendBtn.setStyleSheet(buttonCSS)
		recommendBtn.setText("Recommend")
		recommendBtn.move(320, 525)
		recommendBtn.resize(100, 30)
		recommendBtn.stateChanged.connect(lambda:self.RecommendFn())

	def PrintListFn(self):
		mongoconn = MongoClient("mongodb://localhost:27017")
		print("\r")
		for index in ( mongoconn.Movie.Checklist.find() ):
			print("\033[1m"+index['Title'],"\033[0m | ",index['Director']," | ",index['Year']," | ",index['Language'])

	def CheckExistingFn(self):
		mongoconn = MongoClient("mongodb://localhost:27017")
		query = mongoconn.Movie.Checklist.find({"Title":self.title.text().strip()})
		for i in query:
			if(i['Title'] == self.title.text().strip()):
				ExistingMessage = QtWidgets.QMessageBox()
				ExistingMessage.setText("Already in List")
				ExistingMessage.setWindowTitle("Done!")
				ExistingMessage.exec_()
				return(True)
		mongoconn.close()

	def InsertCheckedFn(self):
		row = {"Title":self.title.text().strip(), "Director":self.director.text().strip(), "Year":self.year.text().strip(), "Language":self.language.currentText(), "Remarks":self.remarks.toPlainText().strip()};
		if(not(self.CheckExistingFn())):
			if(row['Title']==''):
				NullMessage = QtWidgets.QMessageBox()
				NullMessage.setText("No values to enter")
				NullMessage.setWindowTitle("Error!")
				NullMessage.exec_()
			else:
				mongoconn = MongoClient("mongodb://localhost:27017")
				query = mongoconn.Movie.Checklist.update(row, row, upsert = True)
				CheckedMessage = QtWidgets.QMessageBox()
				CheckedMessage.setText("Added to checklist")
				CheckedMessage.setWindowTitle("Done!")
				CheckedMessage.exec_()
				if(recommendBool):
					query = mongoconn.Movie.Recommend.update(row, row, upsert=True)
				mongoconn.close()

	def RecommendFn(self):
		global recommendBool
		recommendBool = not(recommendBool)