import sys
from PyQt5 import QtWidgets, QtGui
import window, checklist

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	app.setWindowIcon(QtGui.QIcon('CamIcon.png'))
	ThisWindow = QtWidgets.QMainWindow()
	window.WindowClass().WindowFn(ThisWindow)
	checklist.ChecklistClass().ChecklistFn(ThisWindow)
	ThisWindow.show()
	sys.exit(app.exec_())