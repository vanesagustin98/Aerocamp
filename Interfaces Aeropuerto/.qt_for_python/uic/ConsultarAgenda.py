# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'consultarAgenda.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Agenda(object):
    def setupUi(self, Agenda):
        if not Agenda.objectName():
            Agenda.setObjectName(u"Agenda")
        Agenda.resize(432, 437)
        Agenda.setStyleSheet(u"background-color: rgb(232, 228, 255);")
        self.centralwidget = QWidget(Agenda)
        self.centralwidget.setObjectName(u"centralwidget")
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(20, 20, 211, 31))
        self.dateEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.bt_consultarAgenda = QPushButton(self.centralwidget)
        self.bt_consultarAgenda.setObjectName(u"bt_consultarAgenda")
        self.bt_consultarAgenda.setGeometry(QRect(280, 20, 131, 31))
        self.bt_consultarAgenda.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.bt_cancelarVuelo = QPushButton(self.centralwidget)
        self.bt_cancelarVuelo.setObjectName(u"bt_cancelarVuelo")
        self.bt_cancelarVuelo.setGeometry(QRect(160, 370, 121, 31))
        self.bt_cancelarVuelo.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.tableWidget = QListWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(135, 81, 151, 271))
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        Agenda.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Agenda)
        self.statusbar.setObjectName(u"statusbar")
        Agenda.setStatusBar(self.statusbar)

        self.retranslateUi(Agenda)

        QMetaObject.connectSlotsByName(Agenda)
    # setupUi

    def retranslateUi(self, Agenda):
        Agenda.setWindowTitle(QCoreApplication.translate("Agenda", u"Agenda de vuelos", None))
        self.bt_consultarAgenda.setText(QCoreApplication.translate("Agenda", u"Consultar", None))
        self.bt_cancelarVuelo.setText(QCoreApplication.translate("Agenda", u"Cancelar", None))
    # retranslateUi

