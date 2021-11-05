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
        Form.resize(410, 303)
        Form.setStyleSheet(u"background-color: rgb(232, 228, 255);")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QRect(260, 70, 111, 31))
        self.pushButton.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QRect(260, 160, 111, 31))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.listView = QTableWidget(Form)
        if (self.listView.columnCount() < 2):
            self.listView.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.listView.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.listView.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(10, 20, 211, 251))
        self.listView.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Listado de Arolineas", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Modificar Aerolinea", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Eliminar Aerolinea", None))
        ___qtablewidgetitem = self.listView.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Nombre", None));
        ___qtablewidgetitem1 = self.listView.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"NIT", None));
    # retranslateUi

