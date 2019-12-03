import sys
from PyQt5 import QtWidgets
from pymongo import MongoClient

class SearchLangClass(object):
	def SearchLangFn(self, window):
		window.setStyleSheet("background-color:rgb(0,0,0);")
		window.setWindowTitle("Search Language")
		window.setFixedSize(500, 500)

		File = open("./css/input.css", 'r')
		inputCSS = File.read().strip()
		File.close()
		File = open("./css/list.css", 'r')
		listCSS = File.read().strip()
		File.close()
		
		self.searchBar = QtWidgets.QComboBox(window)
		self.searchBar.setStyleSheet(inputCSS)
		self.searchBar.resize(120,35)
		self.searchBar.move(190, 45)
		self.searchBar.addItems(('Select','English', 'Tamil', 'Malayalam', 'Hindi', 'Others'))
		self.searchBar.currentTextChanged.connect(lambda: self.PrintLangFn(window, self.searchBar.currentText()))

		self.ListBox = QtWidgets.QTextEdit(window)
		self.ListBox.resize(400, 100)
		self.ListBox.move(50, 180)
		self.ListBox.setStyleSheet(listCSS)

		ListBoxScrollBar = QtWidgets.QScrollBar(self.ListBox)
		ListBoxScrollBar.setStyleSheet("border:none;");
		self.ListBox.setVerticalScrollBar(ListBoxScrollBar)

	def PrintLangFn(self, window, lang):
		self.ListBox.setText("")
		if(lang != "" or lang!="Select"):
			mongoconn = MongoClient("mongodb://localhost:27017")
			for index in (mongoconn.Movie.Checklist.find({"Language": lang})):
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
SearchLangClass().SearchLangFn(MiniWindow)
MiniWindow.show()
sys.exit(miniapp.exec_())