# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vuelo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import logo usuario_rc
import logo usuario_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(574, 421)
        MainWindow.setStyleSheet(u"background-color: rgb(232, 228, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(350, 30, 171, 101))
        self.label_3.setStyleSheet(u"border-image: url(:/cct/iconoprogramarvuelo.jpg);")
        self.crearVuelo = QPushButton(self.centralwidget)
        self.crearVuelo.setObjectName(u"crearVuelo")
        self.crearVuelo.setGeometry(QRect(220, 350, 141, 51))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.crearVuelo.setFont(font)
        self.crearVuelo.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(330, 150, 191, 191))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox_2 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.comboBox_2)

        self.comboBox_3 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.comboBox_3)

        self.comboBox_5 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.comboBox_5)

        self.comboBox_6 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.comboBox_6)

        self.comboBox_4 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.comboBox_4)

        self.formLayoutWidget_6 = QWidget(self.centralwidget)
        self.formLayoutWidget_6.setObjectName(u"formLayoutWidget_6")
        self.formLayoutWidget_6.setGeometry(QRect(60, 170, 221, 161))
        self.formLayout_6 = QFormLayout(self.formLayoutWidget_6)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setVerticalSpacing(20)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.formLayoutWidget_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_19)

        self.dateEdit_3 = QDateEdit(self.formLayoutWidget_6)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.dateEdit_3)

        self.label_21 = QLabel(self.formLayoutWidget_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_21)

        self.dateEdit_4 = QDateEdit(self.formLayoutWidget_6)
        self.dateEdit_4.setObjectName(u"dateEdit_4")
        self.dateEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.dateEdit_4)

        self.label_23 = QLabel(self.formLayoutWidget_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.label_23)

        self.lineEdit_13 = QLineEdit(self.formLayoutWidget_6)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.lineEdit_13)

        self.label_24 = QLabel(self.formLayoutWidget_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.label_24)

        self.comboBox = QComboBox(self.formLayoutWidget_6)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.comboBox)

        self.formLayoutWidget_7 = QWidget(self.centralwidget)
        self.formLayoutWidget_7.setObjectName(u"formLayoutWidget_7")
        self.formLayoutWidget_7.setGeometry(QRect(60, 40, 221, 71))
        self.formLayout_7 = QFormLayout(self.formLayoutWidget_7)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setVerticalSpacing(20)
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.formLayoutWidget_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_20)

        self.timeEdit = QTimeEdit(self.formLayoutWidget_7)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.timeEdit.setMaximumTime(QTime(23, 59, 59))
        self.timeEdit.setCurrentSection(QDateTimeEdit.HourSection)
        self.timeEdit.setTime(QTime(0, 0, 0))

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.timeEdit)

        self.label_22 = QLabel(self.formLayoutWidget_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"background-color: rgb(232, 228, 255);")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_22)

        self.timeEdit_2 = QTimeEdit(self.formLayoutWidget_7)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.timeEdit_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Programar Vuelo", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.crearVuelo.setText(QCoreApplication.translate("MainWindow", u"Crear Vuelo", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccionar Tipo Vuelo", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Pasajeros", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Carga", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccionar Piloto", None))

        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecconar Copiloto", None))

        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccionar Avion", None))

        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccionar Vuelo", None))

        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Fecha Salida", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Fecha llegada", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Cod. Vuelo", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccionar Lugar", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Pasto", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Bogota", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Medellin", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Cali", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Hora Salida", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h:mm", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Hora llegada", None))
        self.timeEdit_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h:mm", None))
    # retranslateUi

