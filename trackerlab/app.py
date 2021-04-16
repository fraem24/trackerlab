# -*- coding: utf-8 -*-

"""
Discription: TrackLab of the Molecular Nanophotonics.
Author(s): M. Fränzl, N. Söker
Data: 18/09/18
"""

import os
      
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QDialog, QMessageBox

from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        path = os.path.dirname(os.path.realpath(__file__))

        self.ui = loadUi(path + '/app.ui', self)        
    
