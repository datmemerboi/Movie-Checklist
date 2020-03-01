import sys
from PyQt5 import QtWidgets
from pymongo import MongoClient

class SearchYearClass(object):
	def SearchYearFn(self, window):
		window.setStyleSheet("background-color:rgb(0,0,0);")
		window.setWindowTitle("Search Year")
		window.setFixedSize(500, 500)

		File = open("./css/input.css", 'r')
		inputCSS = File.read().strip()
		File.close()
		File = open("./css/list.css", 'r')
		listCSS = File.read().strip()
		File.close()
		File = open("./css/count.css", 'r')
		countCSS = File.read().strip()
		File.close()
		
		self.searchBar = QtWidgets.QLineEdit(window)
		self.searchBar.setStyleSheet(inputCSS)
		self.searchBar.resize(100, 45)
		self.searchBar.move(200, 45)
		self.searchBar.setPlaceholderText("Search")
		self.searchBar.textChanged.connect(lambda: self.PrintYearFn(window, self.searchBar.text()))

		self.countText = QtWidgets.QLabel(window)
		self.countText.setStyleSheet(countCSS)
		self.countText.move(200,100)
		self.countText.resize(125,50)

		self.ListBox = QtWidgets.QTextEdit(window)
		self.ListBox.resize(400, 100)
		self.ListBox.move(50, 180)
		self.ListBox.setStyleSheet(listCSS)

		ListBoxScrollBar = QtWidgets.QScrollBar(self.ListBox)
		ListBoxScrollBar.setStyleSheet("border:none;");
		self.ListBox.setVerticalScrollBar(ListBoxScrollBar)

	def PrintYearFn(self, window, year):
		self.ListBox.setText("")
		if(year != ""):
			mongoconn = MongoClient("mongodb://localhost:27017")
			for index in (mongoconn.Movie.Checklist.find({"Year":year})):
				if(self.ListBox.toPlainText().strip()==""):
					self.ListBox.setText(index['Title']+" | "+index['Director']+" | "+index['Year']+" | "+index['Language'])
				else:
					self.ListBox.resize(400, self.ListBox.sizeHint().height()+80)
					self.ListBox.setText(self.ListBox.toPlainText().strip()+"\r\r"+index['Title']+" | "+index['Director']+" | "+index['Year']+" | "+index['Language'])
				if('Remarks' in index and index['Remarks']!=""):
					self.ListBox.setText(self.ListBox.toPlainText().strip()+" | \""+index['Remarks']+"\"")
			self.ListBox.setReadOnly(True)
			self.countText.setText(
				str(mongoconn.Movie.Checklist.find({"Year":year}).count())
				+" records")
			mongoconn.close()

miniapp = QtWidgets.QApplication(sys.argv)
MiniWindow = QtWidgets.QMainWindow()
SearchYearClass().SearchYearFn(MiniWindow)
MiniWindow.show()
sys.exit(miniapp.exec_())