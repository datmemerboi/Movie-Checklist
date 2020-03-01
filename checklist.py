from PyQt5 import QtWidgets
import os, backupnow
import mongo.insert as insert
import FireBase.push as push

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
		searchByDirector.triggered.connect(lambda: os.system("python3 miniwin/printdirector.py"))
		searchByYear = searchMenu.addAction("By Year")
		searchByYear.triggered.connect(lambda: os.system("python3 miniwin/printyear.py"))
		searchByLang = searchMenu.addAction("By Language")
		searchByLang.triggered.connect(lambda: os.system("python3 miniwin/printlanguage.py"))
		
		self.title = QtWidgets.QLineEdit(window)
		self.title.setStyleSheet(inputCSS)
		self.title.resize(350, 45)
		self.title.move(125, 65)
		self.title.setPlaceholderText("Title")

		self.director = QtWidgets.QLineEdit(window)
		self.director.setStyleSheet(inputCSS)
		self.director.resize(350, 45)
		self.director.move(125, 145)
		self.director.setPlaceholderText("Director")

		self.year = QtWidgets.QLineEdit(window)
		self.year.setStyleSheet(inputCSS)
		self.year.resize(100, 45)
		self.year.move(155, 230)
		self.year.setPlaceholderText("Year")

		self.language = QtWidgets.QComboBox(window)
		self.language.addItems(('English', 'Tamil', 'Malayalam', 'Hindi', 'Others'))
		self.language.setStyleSheet(inputCSS)
		self.language.resize(120,35)
		self.language.move(325, 235)

		self.remarks = QtWidgets.QTextEdit(window)
		self.remarks.setStyleSheet(inputCSS+"padding-top:15;")
		self.remarks.setPlaceholderText("Remarks, if any..")
		self.remarks.resize(350, 150)
		self.remarks.move(125, 315)

		recommendBtn = QtWidgets.QCheckBox(window)
		recommendBtn.setChecked(False)
		recommendBtn.setStyleSheet(buttonCSS)
		recommendBtn.resize(125, 30)
		recommendBtn.move(165, 480)
		recommendBtn.setText("Recommend?")
		recommendBtn.stateChanged.connect(lambda:self.RecommendFn())

		self.dbChoose = QtWidgets.QComboBox(window)
		self.dbChoose.setStyleSheet(inputCSS)
		self.dbChoose.addItems(("MongoDB", "Firebase"))
		self.dbChoose.move(315, 480)
		self.dbChoose.resize(120, 30)

		addBtn = QtWidgets.QPushButton(window)
		addBtn.setStyleSheet(buttonCSS)
		addBtn.setText("Add")
		addBtn.resize(70, 30)
		addBtn.move(225, 535)
		addBtn.clicked.connect(lambda: self.WhereToSendFn())

		updateBtn = QtWidgets.QPushButton(window)
		updateBtn.setStyleSheet(buttonCSS)
		updateBtn.setText("Update")
		updateBtn.resize(70, 30)
		updateBtn.move(310, 535)

		printListBtn = QtWidgets.QPushButton(window)
		printListBtn.setStyleSheet(buttonCSS)
		printListBtn.resize(180, 30)
		printListBtn.move(215, 590)
		printListBtn.setText("Print Checklist")
		printListBtn.clicked.connect(lambda: os.system("python3 miniwin/printlist.py"))

	def RecommendFn(self):
		global recommendBool
		recommendBool = not(recommendBool)
	
	def WhereToSendFn(self):
		row = self.NullCheckFn()
		if(row):
			if(self.dbChoose.currentText()=="MongoDB"):
				insert.InsertCheckedFn(row, recommendBool)
			elif(self.dbChoose.currentText()=="Firebase"):
				push.PushToFirebase(row, recommendBool)

	def NullCheckFn(self):
		row = None
		if(self.title.text().strip()=='' or self.director.text().strip()=='' or self.year.text().strip()==''):
			NullMessage = QtWidgets.QMessageBox()
			NullMessage.setText("Missing few values")
			NullMessage.setWindowTitle("Error!")
			NullMessage.exec_()

		elif(self.remarks.toPlainText().strip()==''):
			row = {
			"Title":self.title.text().strip(),
			"Director":self.director.text().strip(),
			"Year":self.year.text().strip(),
			"Language":self.language.currentText()
			}
		else:
			row = {
			"Title":self.title.text().strip(),
			"Director":self.director.text().strip(),
			"Year":self.year.text().strip(),
			"Language":self.language.currentText(),
			"Remarks":self.remarks.toPlainText().strip()
			}
		return row