# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registrarPiloto.ui'
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
        Form.resize(413, 470)
        Form.setStyleSheet(u"background-color: rgb(232, 228, 255);")
        self.bt_registrar_piloto_7 = QPushButton(Form)
        self.bt_registrar_piloto_7.setObjectName(u"bt_registrar_piloto_7")
        self.bt_registrar_piloto_7.setGeometry(QRect(120, 390, 121, 41))
        self.bt_registrar_piloto_7.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 20, 121, 131))
        self.label.setStyleSheet(u"border-image: url(:/cct/iconopiloto.jpg);")
        self.formLayoutWidget_12 = QWidget(Form)
        self.formLayoutWidget_12.setObjectName(u"formLayoutWidget_12")
        self.formLayoutWidget_12.setGeometry(QRect(60, 170, 291, 201))
        self.formLayout_14 = QFormLayout(self.formLayoutWidget_12)
        self.formLayout_14.setObjectName(u"formLayout_14")
        self.formLayout_14.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_14.setFormAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.formLayout_14.setVerticalSpacing(20)
        self.formLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.formLayoutWidget_12)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_14.setWidget(0, QFormLayout.LabelRole, self.label_48)

        self.lineEdit_27 = QLineEdit(self.formLayoutWidget_12)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_14.setWidget(0, QFormLayout.FieldRole, self.lineEdit_27)

        self.label_49 = QLabel(self.formLayoutWidget_12)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_14.setWidget(1, QFormLayout.LabelRole, self.label_49)

        self.lineEdit_28 = QLineEdit(self.formLayoutWidget_12)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_14.setWidget(1, QFormLayout.FieldRole, self.lineEdit_28)

        self.label_50 = QLabel(self.formLayoutWidget_12)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_14.setWidget(2, QFormLayout.LabelRole, self.label_50)

        self.lineEdit_29 = QLineEdit(self.formLayoutWidget_12)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_14.setWidget(2, QFormLayout.FieldRole, self.lineEdit_29)

        self.label_51 = QLabel(self.formLayoutWidget_12)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_14.setWidget(3, QFormLayout.LabelRole, self.label_51)

        self.spinBox_11 = QSpinBox(self.formLayoutWidget_12)
        self.spinBox_11.setObjectName(u"spinBox_11")
        self.spinBox_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_14.setWidget(3, QFormLayout.FieldRole, self.spinBox_11)

        self.label_52 = QLabel(self.formLayoutWidget_12)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_14.setWidget(4, QFormLayout.LabelRole, self.label_52)

        self.dateEdit_10 = QDateEdit(self.formLayoutWidget_12)
        self.dateEdit_10.setObjectName(u"dateEdit_10")
        self.dateEdit_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_14.setWidget(4, QFormLayout.FieldRole, self.dateEdit_10)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.bt_registrar_piloto_7.setText(QCoreApplication.translate("Form", u"Registrar", None))
        self.label.setText("")
        self.label_48.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.label_49.setText(QCoreApplication.translate("Form", u"ID", None))
        self.label_50.setText(QCoreApplication.translate("Form", u"N\u00b0 de licencia", None))
        self.label_51.setText(QCoreApplication.translate("Form", u"Horas de Experiencia", None))
        self.label_52.setText(QCoreApplication.translate("Form", u"Ultima Revision Medica", None))
    # retranslateUi

