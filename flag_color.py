#!/usr/bin/env python

from PyQt4 import QtGui, QtCore
import random
import sys

class FlagColor(QtGui.QColor):
    """Constructor"""
    def __init__(self):
        QtGui.QColor.__init__(self)
        self.color_picker()

    def color_picker(self):
        """Give a random value to setRed, setGreen and setBlue"""
        flagCol = QtGui.QColor(0, 0, 0)
        color = random.randint(1,255)
        colour = random.randint(1,255)
        coulour = random.randint(1,255)
        flagCol.setRed(color)
        flagCol.setGreen(colour)
        flagCol.setBlue(coulour)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    flagcolor = FlagColor()
    app.exec_()
