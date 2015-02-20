#!/usr/bin/env/python

from PyQt4 import QtGui, QtCore
from flag_color import FlagColor
import sys

class FlagUI(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.get_countries()
        self.color_picker()

    def get_countries(self):
        with open("countries_list.txt", "r")as f:
            countries = [line.strip() for line in f]
        for word in countries:
            print("Hello from {}".format(word))

        self.countrylist = QtGui.QComboBox()
        self.countrylist.addItems(countries)

        grid = QtGui.QGridLayout()
        grid.addWidget(self.countrylist, 0, 0)
        self.setLayout(grid)

    def color_picker(self):

        flagCol = QtGui.QColor(0, 0, 0)
        flagCol.setRed(100)
        flagCol.setGreen(50)
        flagCol.setBlue(25)

        self.square = QtGui.QFrame(self)
        self.square.setGeometry(150, 0, 100, 100)
        self.square.setStyleSheet("QFrame { background-color: %s }" % flagCol.name())

        self.setWindowTitle("Flags")
        self.setGeometry(300, 220, 400, 240)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    flags = FlagUI()
    flags.show()
    app.exec_()

