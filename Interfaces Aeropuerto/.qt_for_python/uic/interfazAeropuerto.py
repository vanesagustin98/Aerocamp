# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfazAeropuerto.ui'
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
        Form.resize(523, 455)
        Form.setStyleSheet(u"background-color: rgb(232, 228, 255);")
        self.bt_revisarSoliRegistros = QPushButton(Form)
        self.bt_revisarSoliRegistros.setObjectName(u"bt_revisarSoliRegistros")
        self.bt_revisarSoliRegistros.setGeometry(QRect(30, 200, 211, 61))
        font = QFont()
        font.setPointSize(9)
        self.bt_revisarSoliRegistros.setFont(font)
        self.bt_revisarSoliRegistros.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.bt_solicitudesVuelos = QPushButton(Form)
        self.bt_solicitudesVuelos.setObjectName(u"bt_solicitudesVuelos")
        self.bt_solicitudesVuelos.setGeometry(QRect(280, 200, 211, 61))
        self.bt_solicitudesVuelos.setFont(font)
        self.bt_solicitudesVuelos.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.bt_agendaVuelosAeropuerto = QPushButton(Form)
        self.bt_agendaVuelosAeropuerto.setObjectName(u"bt_agendaVuelosAeropuerto")
        self.bt_agendaVuelosAeropuerto.setGeometry(QRect(30, 290, 211, 61))
        self.bt_agendaVuelosAeropuerto.setFont(font)
        self.bt_agendaVuelosAeropuerto.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.bt_visualizarAerolineas = QPushButton(Form)
        self.bt_visualizarAerolineas.setObjectName(u"bt_visualizarAerolineas")
        self.bt_visualizarAerolineas.setGeometry(QRect(280, 290, 211, 61))
        self.bt_visualizarAerolineas.setFont(font)
        self.bt_visualizarAerolineas.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.bt_cerrarSesion = QPushButton(Form)
        self.bt_cerrarSesion.setObjectName(u"bt_cerrarSesion")
        self.bt_cerrarSesion.setGeometry(QRect(400, 400, 91, 31))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.bt_cerrarSesion.setFont(font1)
        self.bt_cerrarSesion.setStyleSheet(u"color: rgb(85, 0, 127);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 10, 261, 41))
        self.label.setStyleSheet(u"color: rgb(85, 0, 127);")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 60, 191, 121))
        self.label_2.setStyleSheet(u"border-image: url(:/cct/iconoavion.jpg);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"AeroCamp", None))
        self.bt_revisarSoliRegistros.setText(QCoreApplication.translate("Form", u"Revisar Solicitudes de Registro", None))
        self.bt_solicitudesVuelos.setText(QCoreApplication.translate("Form", u"Revisar Solicitudes de Vuelos", None))
        self.bt_agendaVuelosAeropuerto.setText(QCoreApplication.translate("Form", u"Consultar Agenda de Vuelos", None))
        self.bt_visualizarAerolineas.setText(QCoreApplication.translate("Form", u"Visualizar Aerolineas", None))
        self.bt_cerrarSesion.setText(QCoreApplication.translate("Form", u"Cerrar Sesi\u00f3n", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Aeropueto El Campanero</span></p></body></html>", None))
        self.label_2.setText("")
    # retranslateUi

