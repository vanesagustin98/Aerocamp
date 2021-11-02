# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'listadoAerolineas.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(301, 303)
        Form.setStyleSheet(u"background-color: rgb(232, 228, 255);")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QRect(160, 100, 111, 31))
        self.pushButton.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 161, 16))
        self.label.setStyleSheet(u"color: rgb(85, 0, 127);")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QRect(160, 160, 111, 31))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.listView = QListWidget(Form)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(30, 50, 91, 231))
        self.listView.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Listado de Arolineas", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Modificar Aerolinea", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nombre Aerol\u00edneas</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Eliminar Aerolinea", None))
    # retranslateUi

