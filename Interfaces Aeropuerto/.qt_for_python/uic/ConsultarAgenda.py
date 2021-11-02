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
        Agenda.resize(463, 406)
        Agenda.setStyleSheet(u"background-color: rgb(232, 228, 255);")
        self.centralwidget = QWidget(Agenda)
        self.centralwidget.setObjectName(u"centralwidget")
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(30, 60, 251, 31))
        self.dateEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.bt_consultarAgenda = QPushButton(self.centralwidget)
        self.bt_consultarAgenda.setObjectName(u"bt_consultarAgenda")
        self.bt_consultarAgenda.setGeometry(QRect(300, 60, 131, 31))
        self.bt_consultarAgenda.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.bt_cancelarVuelo = QPushButton(self.centralwidget)
        self.bt_cancelarVuelo.setObjectName(u"bt_cancelarVuelo")
        self.bt_cancelarVuelo.setEnabled(True)
        self.bt_cancelarVuelo.setGeometry(QRect(160, 350, 131, 31))
        self.bt_cancelarVuelo.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 20, 241, 16))
        self.label.setStyleSheet(u"color: rgb(85, 0, 127);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 110, 251, 16))
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(85, 0, 127);")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(90, 140, 311, 192))
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
        self.bt_cancelarVuelo.setText(QCoreApplication.translate("Agenda", u"Cancelar Vuelo", None))
        self.label.setText(QCoreApplication.translate("Agenda", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Seleccione la fecha a consultar</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Agenda", u"Seleccione el vuelo que desea cancelar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Agenda", u"Codigo", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Agenda", u"Destino", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Agenda", u"Fecha de salida", None));
    # retranslateUi

