# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import  QIcon
from Widget import *
if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon('favicon.png'))
    #with open('lightblue.css', 'r') as f1:
    #    app.setStyleSheet(f1.read())
    widget=Widget()
    widget.ui.show()
    app.exec_()