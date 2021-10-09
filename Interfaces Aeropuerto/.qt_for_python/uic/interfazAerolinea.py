# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfazAerolinea.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(492, 226)
        MainWindow.setStyleSheet(u"background-color: rgb(232, 228, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.bt_programarVuelo = QPushButton(self.centralwidget)
        self.bt_programarVuelo.setObjectName(u"bt_programarVuelo")
        self.bt_programarVuelo.setGeometry(QRect(30, 50, 121, 61))
        self.bt_programarVuelo.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.bt_solicitarAgendamiento = QPushButton(self.centralwidget)
        self.bt_solicitarAgendamiento.setObjectName(u"bt_solicitarAgendamiento")
        self.bt_solicitarAgendamiento.setGeometry(QRect(190, 50, 121, 61))
        self.bt_solicitarAgendamiento.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.bt_visualizarDatos = QPushButton(self.centralwidget)
        self.bt_visualizarDatos.setObjectName(u"bt_visualizarDatos")
        self.bt_visualizarDatos.setGeometry(QRect(350, 50, 121, 61))
        self.bt_visualizarDatos.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.bt_cerrarSesion = QPushButton(self.centralwidget)
        self.bt_cerrarSesion.setObjectName(u"bt_cerrarSesion")
        self.bt_cerrarSesion.setGeometry(QRect(210, 140, 81, 31))
        self.bt_cerrarSesion.setStyleSheet(u"background-color: rgb(232, 228, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AeroCamp", None))
        self.bt_programarVuelo.setText(QCoreApplication.translate("MainWindow", u"Programar Vuelo", None))
        self.bt_solicitarAgendamiento.setText(QCoreApplication.translate("MainWindow", u"Solicitar Agendamiento", None))
        self.bt_visualizarDatos.setText(QCoreApplication.translate("MainWindow", u"Visualizar Datos", None))
        self.bt_cerrarSesion.setText(QCoreApplication.translate("MainWindow", u"Cerrar Sesion", None))
    # retranslateUi

