# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registrarCopiloto.ui'
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
        Form.resize(413, 467)
        Form.setStyleSheet(u"background-color: rgb(232, 228, 255);")
        self.formLayoutWidget_11 = QWidget(Form)
        self.formLayoutWidget_11.setObjectName(u"formLayoutWidget_11")
        self.formLayoutWidget_11.setGeometry(QRect(60, 170, 291, 201))
        self.formLayout_12 = QFormLayout(self.formLayoutWidget_11)
        self.formLayout_12.setObjectName(u"formLayout_12")
        self.formLayout_12.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_12.setFormAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.formLayout_12.setVerticalSpacing(20)
        self.formLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.formLayoutWidget_11)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_12.setWidget(0, QFormLayout.LabelRole, self.label_43)

        self.lineEdit_24 = QLineEdit(self.formLayoutWidget_11)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_12.setWidget(0, QFormLayout.FieldRole, self.lineEdit_24)

        self.label_44 = QLabel(self.formLayoutWidget_11)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_12.setWidget(1, QFormLayout.LabelRole, self.label_44)

        self.lineEdit_25 = QLineEdit(self.formLayoutWidget_11)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_12.setWidget(1, QFormLayout.FieldRole, self.lineEdit_25)

        self.label_45 = QLabel(self.formLayoutWidget_11)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_12.setWidget(2, QFormLayout.LabelRole, self.label_45)

        self.lineEdit_26 = QLineEdit(self.formLayoutWidget_11)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_12.setWidget(2, QFormLayout.FieldRole, self.lineEdit_26)

        self.label_46 = QLabel(self.formLayoutWidget_11)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_12.setWidget(3, QFormLayout.LabelRole, self.label_46)

        self.spinBox_10 = QSpinBox(self.formLayoutWidget_11)
        self.spinBox_10.setObjectName(u"spinBox_10")
        self.spinBox_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_12.setWidget(3, QFormLayout.FieldRole, self.spinBox_10)

        self.label_47 = QLabel(self.formLayoutWidget_11)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_12.setWidget(4, QFormLayout.LabelRole, self.label_47)

        self.dateEdit_9 = QDateEdit(self.formLayoutWidget_11)
        self.dateEdit_9.setObjectName(u"dateEdit_9")
        self.dateEdit_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_12.setWidget(4, QFormLayout.FieldRole, self.dateEdit_9)

        self.bt_registrar_piloto_7 = QPushButton(Form)
        self.bt_registrar_piloto_7.setObjectName(u"bt_registrar_piloto_7")
        self.bt_registrar_piloto_7.setGeometry(QRect(130, 390, 121, 41))
        self.bt_registrar_piloto_7.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 20, 121, 131))
        self.label.setStyleSheet(u"image: url(:/cct/iconopiloto.jpg);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_43.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.label_44.setText(QCoreApplication.translate("Form", u"ID", None))
        self.label_45.setText(QCoreApplication.translate("Form", u"N\u00b0 de licencia", None))
        self.label_46.setText(QCoreApplication.translate("Form", u"Horas de Experiencia", None))
        self.label_47.setText(QCoreApplication.translate("Form", u"Ultima Revision Medica", None))
        self.bt_registrar_piloto_7.setText(QCoreApplication.translate("Form", u"Registrar", None))
        self.label.setText("")
    # retranslateUi

