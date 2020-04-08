# Window of entire recommended list
# ShowRecommendedClass.ShowRecommendedFn() will create the UI and display the recommended list


import sys, os
from PyQt5 import QtWidgets
from pymongo import MongoClient

class ShowRecommendedClass(object):
	def ShowRecommendedFn(self, window):
		window.setFixedSize(600, 600)
		window.setStyleSheet("background-color:rgb(0,0,0);")
		window.setWindowTitle("Your Recommended List")

		path = os.path.join( os.path.dirname(__file__), "..", "css/" )
		
		File = open(path+"list.css", 'r')
		listCSS = File.read().strip()
		File.close()

		ListBox = QtWidgets.QTextEdit(window)
		ListBox.resize(600, 100)
		ListBox.setStyleSheet(listCSS)

		ListBoxScrollBar = QtWidgets.QScrollBar(ListBox)
		ListBoxScrollBar.setStyleSheet("border:none; font-size:100px;")
		ListBox.setVerticalScrollBar(ListBoxScrollBar)
		
		mongoconn = MongoClient("mongodb://localhost:27017")
		for index in ( mongoconn.Movie.Recommend.find() ):
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
ShowRecommendedClass().ShowRecommendedFn(MiniWindow)
MiniWindow.show()
sys.exit(miniapp.exec_())