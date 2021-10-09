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
        Form.resize(473, 348)
        Form.setStyleSheet(u"background-color: rgb(232, 228, 255);")
        self.tableView = QTableView(Form)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(60, 50, 341, 221))
        self.tableView.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 300, 111, 31))
        self.pushButton.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 161, 16))
        self.label.setStyleSheet(u"color: rgb(85, 0, 127);")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(270, 300, 101, 31))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(170, 170, 255);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Listado de Arolineas", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Modificar Aerolinea", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Listado de Aeroineas</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Eliminar Aerolinea", None))
    # retranslateUi

