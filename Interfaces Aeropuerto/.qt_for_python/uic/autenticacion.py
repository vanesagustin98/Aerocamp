# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'autenticacion.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import logo usuario_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(453, 331)
        MainWindow.setStyleSheet(u"background-color: rgb(232, 228, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(260, 40, 151, 21))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(260, 80, 151, 21))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 140, 141, 51))
        self.pushButton.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 20, 101, 101))
        self.label_2.setStyleSheet(u"border-image: url(:/cct/iconoiniciosesion.jpg);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 40, 51, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(180, 80, 71, 16))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(160, 260, 191, 23))
        font = QFont()
        font.setUnderline(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"color: rgb(85, 0, 127);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 210, 111, 101))
        self.label.setStyleSheet(u"border-image: url(:/cct/iconoformulario.jpg);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Autenticacion de Usuario", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Iniciar Sesion", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Formulario de Registro Aerolinea", None))
        self.label.setText("")
    # retranslateUi

