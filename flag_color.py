#!/usr/bin/env python

from PyQt4 import QtGui, QtCore
import sys
from random import randrange

class FlagColor(QtGui.QColor):
    """Constructor"""
    def __init__(self):
        QtGui.QColor.__init__(self)

    def color_picker(self):

        self.col = QtGui.QtColor(0, 0, 0)
        val = randrange(255)
        self.col.setRed(val)
        self.col.setGreen(val)
        self.col.setBlue(val)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    flagcolor = FlagColor()
    flagcolor.show()
    app.exec_()
