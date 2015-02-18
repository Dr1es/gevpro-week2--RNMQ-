#!/usr/bin/env/python

from PyQt4 import QtGui, QtCore
from flag_color import FlagColor
import sys

class FlagUI(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setWindowTitle("Flags")
		self.get_countries()
		
	def get_countries(self):
		with open("countries_list.txt", "r")as f:
			countries = [line.strip() for line in f]
		for word in countries:
			print("Hello from {}".format(word))
			
		#self.countries = QtGui.QCombobox()
		#self.countries.addItems(countries)
	
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
