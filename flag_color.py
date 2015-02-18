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
        r = self.col.setRed(range(255))
        g = self.col.setGreen(range(255))
        b = self.col.setBlue(range(255))

        
        self.square.setStyleSheet("QFrame { background-color: %s }" % FlagColor.name())
        return (r,g,b)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    flagcolor = FlagColor()
    #flagcolor.show()
    app.exec_()
