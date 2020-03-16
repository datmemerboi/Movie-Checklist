import sys
from PyQt5 import QtWidgets
from pymongo import MongoClient

class UpdateWindowClass(object):
	def UpdateWindowFn(self, window):
		window.setStyleSheet("background-color:rgb(0,0,0);")
		window.setWindowTitle("Updation")
		window.setFixedSize(700, 700)

		File = open("../css/input.css", 'r'); inputCSS = File.read().strip(); File.close();
		File = open("../css/button.css", 'r'); buttonCSS = File.read().strip(); File.close();
		
		self.fromTitle = QtWidgets.QLineEdit(window)
		self.fromTitle.setStyleSheet(inputCSS)
		self.fromTitle.resize(280, 45)
		self.fromTitle.move(55, 60)
		self.fromTitle.setPlaceholderText("Old Title")
		self.fromTitle.textChanged.connect(lambda: self.FillOld())

		self.fromDirector = QtWidgets.QLineEdit(window)
		self.fromDirector.setStyleSheet(inputCSS)
		self.fromDirector.resize(280, 45)
		self.fromDirector.move(55, 150)
		self.fromDirector.setPlaceholderText("Old Director")

		self.fromYear = QtWidgets.QLineEdit(window)
		self.fromYear.setStyleSheet(inputCSS)
		self.fromYear.resize(100, 45)
		self.fromYear.move(140, 230)
		self.fromYear.setPlaceholderText("Old Year")

		self.fromLang = QtWidgets.QComboBox(window)
		self.fromLang.setStyleSheet(inputCSS)
		self.fromLang.resize(120,35)
		self.fromLang.move(130, 320)
		self.fromLang.addItems(('English', 'Tamil', 'Malayalam', 'Hindi', 'Others'))

		self.fromRemarks = QtWidgets.QTextEdit(window)
		self.fromRemarks.setStyleSheet(inputCSS+"padding-top:15;")
		self.fromRemarks.setPlaceholderText("Old Remarks")
		self.fromRemarks.resize(260, 120)
		self.fromRemarks.move(70, 400)

		self.toTitle = QtWidgets.QLineEdit(window)
		self.toTitle.setStyleSheet(inputCSS)
		self.toTitle.resize(280, 45)
		self.toTitle.move(360, 60)
		self.toTitle.setPlaceholderText("New Title")

		self.toDirector = QtWidgets.QLineEdit(window)
		self.toDirector.setStyleSheet(inputCSS)
		self.toDirector.resize(280, 45)
		self.toDirector.move(360, 150)
		self.toDirector.setPlaceholderText("New Director")

		self.toYear = QtWidgets.QLineEdit(window)
		self.toYear.setStyleSheet(inputCSS)
		self.toYear.resize(100, 45)
		self.toYear.move(435, 230)
		self.toYear.setPlaceholderText("New Year")

		self.toLang = QtWidgets.QComboBox(window)
		self.toLang.setStyleSheet(inputCSS)
		self.toLang.resize(120,35)
		self.toLang.move(430, 320)
		self.toLang.addItems(('English', 'Tamil', 'Malayalam', 'Hindi', 'Others'))

		self.toRemarks = QtWidgets.QTextEdit(window)
		self.toRemarks.setStyleSheet(inputCSS+"padding-top:15;")
		self.toRemarks.setPlaceholderText("New Remarks")
		self.toRemarks.resize(260, 120)
		self.toRemarks.move(370, 400)

		LtoRbtn = QtWidgets.QPushButton(window)
		LtoRbtn.setText("L to R")
		LtoRbtn.setStyleSheet(buttonCSS)
		LtoRbtn.resize(100, 40)
		LtoRbtn.move(300, 560)

	def FillOld(self):
		mongoconn = MongoClient("mongodb://localhost:27017")
		query = mongoconn.Movie.Checklist.find(
			{"Title": {"$regex":self.fromTitle.text().strip(), "$options":'i'} }
			);
		if(query.count()==1):
			for result in query:
				self.fromTitle.setText(result['Title'])
				self.fromDirector.setText(result['Director'])
				self.fromYear.setText(result['Year'])
				index = self.fromLang.findText(result['Language']) 
				self.fromLang.setCurrentIndex(index)
				if(result['Remarks']!=None):
					self.fromRemarks.setText(result['Remarks'])


miniapp = QtWidgets.QApplication(sys.argv)
MiniWindow = QtWidgets.QMainWindow()
UpdateWindowClass().UpdateWindowFn(MiniWindow)
MiniWindow.show()
sys.exit(miniapp.exec_())