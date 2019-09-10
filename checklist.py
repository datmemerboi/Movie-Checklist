from PyQt5 import QtWidgets, QtCore
from pymongo import MongoClient

class ChecklistClass(object):
	def ChecklistFn(self, window):
		window.setWindowTitle("Movie Checklist")

		pushy = QtWidgets.QPushButton(window)
		pushy.setStyleSheet("background-color:white")
		pushy.move(500, 0)
		pushy.setText("Print")
		pushy.clicked.connect(lambda: self.PrintList())

		File = open("css/input.css", 'r')
		inputCSS = File.read().strip()
		File.close()

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

		CheckBtn = QtWidgets.QPushButton(window)
		CheckBtn.setStyleSheet("background-color:white;color:black;")
		CheckBtn.move(235, 525)
		CheckBtn.setText("Check")
		CheckBtn.clicked.connect(lambda: self.InsertChecked())

	def PrintList(self):
		mongoconn = MongoClient("mongodb://localhost:27017")
		print("Printing List:")
		for index in ( mongoconn.Movie.Checklist.find() ):
			print(index)

	def InsertChecked(self):
		mongoconn = MongoClient("mongodb://localhost:27017")
		row = {"Title":self.title.text().strip(), "Director":self.director.text().strip(), "Year":self.year.text().strip(), "Language":self.language.currentText(), "Remarks":self.remarks.toPlainText().strip()};
		query = mongoconn.Movie.Checklist.update(row, row, upsert = True)
		print("-- New Item Added --")
		CheckedMessage = QtWidgets.QMessageBox()
		CheckedMessage.setText("Checked!")
		CheckedMessage.setWindowTitle(" ")
		CheckedMessage.exec_()