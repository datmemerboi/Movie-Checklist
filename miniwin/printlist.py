import sys
from PyQt5 import QtWidgets
from pymongo import MongoClient
class PrintListClass(object):
	def PrintListFn(self, window):
		window.setFixedSize(600, 600)
		window.setStyleSheet("background-color:rgb(0,0,0);")
		window.setWindowTitle("Your Current List")

		File = open("./css/list.css", 'r')
		listCSS = File.read().strip()
		File.close()

		ListBox = QtWidgets.QTextEdit(window)
		ListBox.resize(600, 100)
		ListBox.setStyleSheet(listCSS)

		ListBoxScrollBar = QtWidgets.QScrollBar(ListBox)
		ListBoxScrollBar.setStyleSheet("border:none;")
		ListBox.setVerticalScrollBar(ListBoxScrollBar)
		
		mongoconn = MongoClient("mongodb://localhost:27017")
		for index in ( mongoconn.Movie.Checklist.find() ):
			if(ListBox.toPlainText().strip()==""):
				ListBox.setText(index['Title']+" | "+index['Director']+" | "+index['Year']+" | "+index['Language'])
			else:
				ListBox.resize(600, ListBox.sizeHint().height()+400)
				ListBox.setText(ListBox.toPlainText().strip()+"\n\n"+index['Title']+" | "+index['Director']+" | "+index['Year']+" | "+index['Language'])
			if('Remarks' in index and index['Remarks']!=""):
				ListBox.setText(ListBox.toPlainText().strip()+" | \""+index['Remarks']+"\"")
		ListBox.setReadOnly(True)
		mongoconn.close()

miniapp = QtWidgets.QApplication(sys.argv)
MiniWindow = QtWidgets.QMainWindow()
PrintListClass().PrintListFn(MiniWindow)
MiniWindow.show()
sys.exit(miniapp.exec_())