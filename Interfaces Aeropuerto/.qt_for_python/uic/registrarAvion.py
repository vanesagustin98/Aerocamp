# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registrarAvion.ui'
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
        Form.resize(556, 464)
        Form.setStyleSheet(u"background-color: rgb(232, 228, 255);")
        self.formLayoutWidget_5 = QWidget(Form)
        self.formLayoutWidget_5.setObjectName(u"formLayoutWidget_5")
        self.formLayoutWidget_5.setGeometry(QRect(50, 140, 471, 221))
        self.formLayout_5 = QFormLayout(self.formLayoutWidget_5)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_5.setVerticalSpacing(20)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.formLayoutWidget_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.lineEdit = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_14 = QLabel(self.formLayoutWidget_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.lineEdit_2 = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.lineEdit_10 = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.lineEdit_10)

        self.label_17 = QLabel(self.formLayoutWidget_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.label_17)

        self.lineEdit_11 = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.lineEdit_11)

        self.label_18 = QLabel(self.formLayoutWidget_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_5.setWidget(5, QFormLayout.LabelRole, self.label_18)

        self.lineEdit_12 = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_5.setWidget(5, QFormLayout.FieldRole, self.lineEdit_12)

        self.label_15 = QLabel(self.formLayoutWidget_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_15)

        self.label_16 = QLabel(self.formLayoutWidget_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_16)

        self.comboBox_2 = QComboBox(self.formLayoutWidget_5)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.comboBox_2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 10, 121, 111))
        self.label.setStyleSheet(u"border-image: url(:/cct/iconoregistroavion.jpg);")
        self.bt_registrar_piloto_7 = QPushButton(Form)
        self.bt_registrar_piloto_7.setObjectName(u"bt_registrar_piloto_7")
        self.bt_registrar_piloto_7.setGeometry(QRect(230, 390, 121, 41))
        self.bt_registrar_piloto_7.setStyleSheet(u"background-color: rgb(170, 170, 255);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"ID. Avion", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Modelo", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Peso Nominal", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Capacidad", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Tipo propulsion", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"N\u00b0 Motor", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"Seleccionar Tipo Propulsion", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"Reacci\u00f3n", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Form", u"Turbo H\u00e9lice", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Form", u"H\u00e9lice", None))

        self.label.setText("")
        self.bt_registrar_piloto_7.setText(QCoreApplication.translate("Form", u"Registrar", None))
    # retranslateUi

