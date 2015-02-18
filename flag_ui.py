#!/usr/bin/env/python

from PyQt4 import QtGui, QtCore
import sys

class FlagUI(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setWindowTitle("Flags")
	
	def color_picker(self):
		
		self.col = QtGui.QtColor(0, 0, 0)
		self.col.setRed(100)
		self.col.setGreen(50)
		self.col.setBlue(25)
		
		self.square.setStyleSheet("QFrame { background-color: %s }" % FlagColor.name())
	
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	flags = FlagUI()
	flags.show()
	app.exec_()
