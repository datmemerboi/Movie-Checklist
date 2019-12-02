import sys
from PyQt5 import QtWidgets
from pymongo import MongoClient

class DirectorWorksClass(object):
	def DirectorWorksFn(self, window):
		window.setStyleSheet("background-color:rgb(0,0,0);")
		window.setWindowTitle("Director Works")
		window.setFixedSize(500, 500)

		File = open("./css/input.css", 'r')
		inputCSS = File.read().strip()
		File.close()
		File = open("./css/list.css", 'r')
		listCSS = File.read().strip()
		File.close()
		
		self.searchBar = QtWidgets.QLineEdit(window)
		self.searchBar.setStyleSheet(inputCSS)
		self.searchBar.resize(300, 45)
		self.searchBar.move(105, 45)
		self.searchBar.setPlaceholderText("Search for Director's Works")
		self.searchBar.textChanged.connect(lambda: self.PrintDirectorFn(window, self.searchBar.text()))

		self.ListBox = QtWidgets.QTextEdit(window)
		self.ListBox.resize(400, 100)
		self.ListBox.move(50, 180)
		self.ListBox.setStyleSheet(listCSS)

		ListBoxScrollBar = QtWidgets.QScrollBar(self.ListBox)
		ListBoxScrollBar.setStyleSheet("border:none;");
		self.ListBox.setVerticalScrollBar(ListBoxScrollBar)

	def PrintDirectorFn(self, window, director):
		self.ListBox.setText("")
		if(director != ""):
			mongoconn = MongoClient("mongodb://localhost:27017")
			for index in (mongoconn.Movie.Checklist.find({"Director":{'$regex' : director, '$options' : 'i'}})):
				if(self.ListBox.toPlainText().strip()==""):
					self.ListBox.setText(index['Title']+" | "+index['Director']+" | "+index['Year']+" | "+index['Language'])
				else:
					self.ListBox.resize(400, self.ListBox.sizeHint().height()+80)
					self.ListBox.setText(self.ListBox.toPlainText().strip()+"\r\r"+index['Title']+" | "+index['Director']+" | "+index['Year']+" | "+index['Language'])
				if('Remarks' in index and index['Remarks']!=""):
					self.ListBox.setText(self.ListBox.toPlainText().strip()+" | \""+index['Remarks']+"\"")
			self.ListBox.setReadOnly(True)
			mongoconn.close()

miniapp = QtWidgets.QApplication(sys.argv)
MiniWindow = QtWidgets.QMainWindow()
DirectorWorksClass().DirectorWorksFn(MiniWindow)
MiniWindow.show()
sys.exit(miniapp.exec_())