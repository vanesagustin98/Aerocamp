# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formularioRegistro.ui'
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
        Form.resize(476, 280)
        Form.setStyleSheet(u"background-color: rgb(232, 228, 255);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 20, 91, 20))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 60, 91, 20))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 100, 91, 20))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 140, 91, 20))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 180, 81, 20))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 220, 121, 41))
        self.pushButton.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(310, 20, 141, 20))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(310, 60, 141, 20))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(310, 100, 141, 22))
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(310, 140, 141, 20))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(310, 180, 141, 20))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 50, 131, 131))
        self.label_6.setStyleSheet(u"border-image: url(:/cct/iconoformulario.jpg);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Formulario De Registro", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nombre Aerol\u00ednea", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"NIT. Arolinea", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Ciudad", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Correo Electronico", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Telefono", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Enviar", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Selccionar Ciudad", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Pasto", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Bogota", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"Medellin", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"Cali", None))

        self.label_6.setText("")
    # retranslateUi

