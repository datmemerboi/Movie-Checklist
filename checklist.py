from PyQt5 import QtWidgets
from pymongo import MongoClient
import os, backupnow
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
		File = open("./css/menubar.css",'r')
		menubarCSS = File.read().strip()
		File.close()
		File = open("./css/label.css", 'r')
		labelCSS = File.read().strip()
		File.close()

		menuBar = window.menuBar()
		menuBar.setStyleSheet(menubarCSS)

		backupMenu = menuBar.addMenu("Backup")
		backupChecklistMenu = backupMenu.addAction("Backup Checklist")
		backupChecklistMenu.triggered.connect(lambda: backupnow.BackupNowFn("Movie", "Checklist"))
		backupRecommendedMenu = backupMenu.addAction("Backup Recommended")
		backupRecommendedMenu.triggered.connect(lambda: backupnow.BackupNowFn("Movie", "Recommend"))

		searchMenu = menuBar.addMenu("Search")
		searchByDirector = searchMenu.addAction("By Director")
		searchByDirector.triggered.connect(lambda: os.system("python3 printdirector.py"))
		searchByYear = searchMenu.addAction("By Year")
		searchByYear.triggered.connect(lambda: os.system("python3 printyear.py"))
		searchByLang = searchMenu.addAction("By Language")
		searchByLang.triggered.connect(lambda: os.system("python3 printlanguage.py"))
		
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

		addBtn = QtWidgets.QPushButton(window)
		addBtn.setStyleSheet(buttonCSS)
		addBtn.setText("Add")
		addBtn.resize(70, 30)
		addBtn.move(230, 525)
		addBtn.clicked.connect(lambda: self.CheckExistingFn())
		addBtn.clicked.connect(lambda: self.InsertCheckedFn())

		recommendBtn = QtWidgets.QCheckBox(window)
		recommendBtn.setChecked(False)
		recommendBtn.setStyleSheet(buttonCSS)
		recommendBtn.resize(15, 30)
		recommendBtn.move(320, 480)
		recommendBtn.stateChanged.connect(lambda:self.RecommendFn())
		recommendText = QtWidgets.QLabel(window)
		recommendText.setText("Recommend?")
		recommendText.setStyleSheet(labelCSS)
		recommendText.move(340, 478)

		printListBtn = QtWidgets.QPushButton(window)
		printListBtn.setStyleSheet(buttonCSS)
		printListBtn.resize(180, 30)
		printListBtn.move(215, 540)
		printListBtn.setText("Print Checklist")
		printListBtn.clicked.connect(lambda: os.system("python3 printlist.py"))

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

	def RecommendFn(self):
		global recommendBool
		recommendBool = not(recommendBool)