# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WidgetForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(963, 695)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.plainTextEdit = QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_2.addWidget(self.plainTextEdit)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plainTextEdit_2 = QPlainTextEdit(self.groupBox)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")

        self.verticalLayout.addWidget(self.plainTextEdit_2)


        self.verticalLayout_3.addWidget(self.groupBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.plainTextEdit_3 = QPlainTextEdit(self.groupBox_3)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")

        self.verticalLayout_4.addWidget(self.plainTextEdit_3)


        self.verticalLayout_6.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.plainTextEdit_4 = QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")

        self.verticalLayout_5.addWidget(self.plainTextEdit_4)


        self.verticalLayout_6.addWidget(self.groupBox_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout.addWidget(self.pushButton_8)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout.addWidget(self.pushButton_7)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 963, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RSA\u5de5\u5177", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u79c1\u94a5\uff1a", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u516c\u94a5\uff1a", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u660e\u6587\uff1a", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5bc6\u6587\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u94a5\u4f4d\u6570\uff1a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1024", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2048", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"4096", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u5bc6\u94a5\u5bf9", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u79c1\u94a5\u751f\u6210\u516c\u94a5", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u79c1\u94a5", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u516c\u94a5", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8f7d\u5165\u79c1\u94a5", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8f7d\u5165\u516c\u94a5", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u516c\u94a5\u52a0\u5bc6", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u79c1\u94a5\u89e3\u5bc6", None))
    # retranslateUi

