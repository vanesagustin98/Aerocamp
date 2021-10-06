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


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(411, 269)
        Form.setStyleSheet(u"background-color: rgb(232, 228, 255);")
        self.bt_revisarSoliRegistros = QPushButton(Form)
        self.bt_revisarSoliRegistros.setObjectName(u"bt_revisarSoliRegistros")
        self.bt_revisarSoliRegistros.setGeometry(QRect(30, 30, 161, 61))
        self.bt_revisarSoliRegistros.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.bt_solicitudesVuelos = QPushButton(Form)
        self.bt_solicitudesVuelos.setObjectName(u"bt_solicitudesVuelos")
        self.bt_solicitudesVuelos.setGeometry(QRect(220, 30, 161, 61))
        self.bt_solicitudesVuelos.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.bt_agendaVuelosAeropuerto = QPushButton(Form)
        self.bt_agendaVuelosAeropuerto.setObjectName(u"bt_agendaVuelosAeropuerto")
        self.bt_agendaVuelosAeropuerto.setGeometry(QRect(30, 120, 161, 61))
        self.bt_agendaVuelosAeropuerto.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.bt_visualizarAerolineas = QPushButton(Form)
        self.bt_visualizarAerolineas.setObjectName(u"bt_visualizarAerolineas")
        self.bt_visualizarAerolineas.setGeometry(QRect(220, 120, 161, 61))
        self.bt_visualizarAerolineas.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.bt_cerrarSesion = QPushButton(Form)
        self.bt_cerrarSesion.setObjectName(u"bt_cerrarSesion")
        self.bt_cerrarSesion.setGeometry(QRect(160, 200, 91, 41))
        self.bt_cerrarSesion.setStyleSheet(u"color: rgb(85, 0, 127);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"AeroCamp", None))
        self.bt_revisarSoliRegistros.setText(QCoreApplication.translate("Form", u"Revisar Solicitudes de Registro", None))
        self.bt_solicitudesVuelos.setText(QCoreApplication.translate("Form", u"Revisar Solicitudes de Vuelos", None))
        self.bt_agendaVuelosAeropuerto.setText(QCoreApplication.translate("Form", u"Consultar Agenda de Vuelos", None))
        self.bt_visualizarAerolineas.setText(QCoreApplication.translate("Form", u"Visualizar Aerolineas", None))
        self.bt_cerrarSesion.setText(QCoreApplication.translate("Form", u"Cerrar Sesion", None))
    # retranslateUi

