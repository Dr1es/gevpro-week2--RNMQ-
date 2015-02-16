#!/usr/bin/env python

from PyQt4 import QtGui,QtCore
import sys

class FlagColor(QtGui.QColor):
    """Constructor"""
    def __init__(self):
        QtGui.QColor.__init__(self)








if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    flagcolor = FlagColor()
    flagcolor.show()
    app.exec_()
