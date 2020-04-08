# Create a Mini Window to Search particular title in checklist
# SearchListClass.SearchListFn() will create the UI
# PrintTitleFn(Window, Title) will display the records with the Title in Window

import sys, os
from PyQt5 import QtWidgets
from pymongo import MongoClient

class SearchListClass(object):
	def SearchListFn(self, window):
		window.setStyleSheet("background-color:rgb(0,0,0);")
		window.setWindowTitle("Search Checklist")
		window.setFixedSize(500, 500)

		path = os.path.join( os.path.dirname(__file__), "..", "css/" )
		File = open(path+"input.css", 'r')
		inputCSS = File.read().strip()
		File.close()
		File = open(path+"list.css", 'r')
		listCSS = File.read().strip()
		File.close()
		File = open(path+"count.css", 'r')
		countCSS = File.read().strip()
		File.close()

		self.searchBar = QtWidgets.QLineEdit(window)
		self.searchBar.setStyleSheet(inputCSS)
		self.searchBar.resize(300, 45)
		self.searchBar.move(105, 45)
		self.searchBar.setPlaceholderText("Search term in checklist")
		self.searchBar.textChanged.connect(lambda: self.PrintTitleFn(window, self.searchBar.text()))

		self.countText = QtWidgets.QLabel(window)
		self.countText.setStyleSheet(countCSS)
		self.countText.move(190,100)
		self.countText.resize(130,50)

		self.ListBox = QtWidgets.QTextEdit(window)
		self.ListBox.resize(400, 100)
		self.ListBox.move(50, 180)
		self.ListBox.setStyleSheet(listCSS)

		ListBoxScrollBar = QtWidgets.QScrollBar(self.ListBox)
		ListBoxScrollBar.setStyleSheet("border:none;");
		self.ListBox.setVerticalScrollBar(ListBoxScrollBar)

	def PrintTitleFn(self, window, title):
		self.ListBox.setText(""); self.countText.setText("")
		if(title != ""):
			mongoconn = MongoClient("mongodb://localhost:27017")
			for record in (mongoconn.Movie.Checklist.find({"Title":{'$regex' : title, '$options' : 'i'}})):
				if(self.ListBox.toPlainText().strip()==""):
					self.ListBox.setText(record['Title']+" | "+record['Director']+" | "+record['Year']+" | "+record['Language'])
				else:
					self.ListBox.resize(400, self.ListBox.sizeHint().height()+80)
					self.ListBox.setText(self.ListBox.toPlainText().strip()+"\r\r"+record['Title']+" | "+record['Director']+" | "+record['Year']+" | "+record['Language'])
				if('Remarks' in record and record['Remarks']!=""):
					self.ListBox.setText(self.ListBox.toPlainText().strip()+" | \""+record['Remarks']+"\"")
			self.ListBox.setReadOnly(True)
			self.countText.setText(
				str(mongoconn.Movie.Checklist.find({"Title":{'$regex' : title, '$options' : 'i'}}).count())
				+" records")
			mongoconn.close()

miniapp = QtWidgets.QApplication(sys.argv)
MiniWindow = QtWidgets.QMainWindow()
SearchListClass().SearchListFn(MiniWindow)
MiniWindow.show()
sys.exit(miniapp.exec_())