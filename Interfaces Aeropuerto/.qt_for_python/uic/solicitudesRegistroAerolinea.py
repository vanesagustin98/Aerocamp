# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'solicitudesRegistroAerolinea.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import logo usuario_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(585, 245)
        Form.setStyleSheet(u"background-color: rgb(232, 228, 255);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 20, 281, 41))
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(200, 90, 311, 22))
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 150, 131, 41))
        self.pushButton.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(370, 150, 141, 41))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 30, 111, 131))
        self.label_2.setStyleSheet(u"image: url(:/cct/iconosolicitudregistro.jpg);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Solicitudes Registro Aeolinea", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Selecciona el Nombre de la Aerolinea</span></p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Seleccionar Aerolinea", None))

        self.pushButton.setText(QCoreApplication.translate("Form", u"Crear Usuario Aerolinea", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Rechazar Solicitud", None))
        self.label_2.setText("")
    # retranslateUi

