# Entry point of application. Run python3 index.py to launch application

import sys, window, checklist
from PyQt5 import QtWidgets, QtGui

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	app.setWindowIcon(QtGui.QIcon('CamIcon.png'))
	ThisWindow = QtWidgets.QMainWindow()
	window.WindowClass().WindowFn(ThisWindow)
	checklist.ChecklistClass().ChecklistFn(ThisWindow)
	ThisWindow.show()
	sys.exit(app.exec_())