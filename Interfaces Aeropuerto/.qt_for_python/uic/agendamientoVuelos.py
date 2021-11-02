# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agendamientoVuelos.ui'
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
        Form.resize(702, 470)
        Form.setStyleSheet(u"background-color: rgb(232, 228, 255);")
        self.bt_realizarSolicitud = QPushButton(Form)
        self.bt_realizarSolicitud.setObjectName(u"bt_realizarSolicitud")
        self.bt_realizarSolicitud.setGeometry(QRect(100, 380, 211, 41))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(170, 170, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(212, 212, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(85, 85, 127, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(113, 113, 170, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.bt_realizarSolicitud.setPalette(palette)
        self.bt_realizarSolicitud.setTabletTracking(False)
        self.bt_realizarSolicitud.setAutoFillBackground(False)
        self.bt_realizarSolicitud.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.bt_realizarSolicitud.setInputMethodHints(Qt.ImhNone)
        self.bt_modificarDatos = QPushButton(Form)
        self.bt_modificarDatos.setObjectName(u"bt_modificarDatos")
        self.bt_modificarDatos.setEnabled(True)
        self.bt_modificarDatos.setGeometry(QRect(430, 280, 181, 41))
        self.bt_modificarDatos.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.bt_eliminarVuelo = QPushButton(Form)
        self.bt_eliminarVuelo.setObjectName(u"bt_eliminarVuelo")
        self.bt_eliminarVuelo.setEnabled(True)
        self.bt_eliminarVuelo.setGeometry(QRect(450, 330, 141, 31))
        self.bt_eliminarVuelo.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 361, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(85, 0, 127);")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(460, 130, 121, 141))
        self.label_2.setPixmap(QPixmap(u":/cct/iconoagenda.jpg"))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(400, 50, 261, 71))
        self.ls_vuelos = QTableWidget(Form)
        if (self.ls_vuelos.columnCount() < 3):
            self.ls_vuelos.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.ls_vuelos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ls_vuelos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.ls_vuelos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.ls_vuelos.setObjectName(u"ls_vuelos")
        self.ls_vuelos.setGeometry(QRect(30, 70, 341, 281))
        self.ls_vuelos.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Agendamiento de Vuelos", None))
        self.bt_realizarSolicitud.setText(QCoreApplication.translate("Form", u"Realizar Solicitud de Agendamiento", None))
        self.bt_modificarDatos.setText(QCoreApplication.translate("Form", u"Modificar Datos de Vuelo", None))
        self.bt_eliminarVuelo.setText(QCoreApplication.translate("Form", u"Eliminar Vuelo", None))
        self.label.setText(QCoreApplication.translate("Form", u"Seleccione el vuelo que desesa agendar", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Recuerda que los vuelos ademas de ser </span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">agendados, tambien pueden ser </span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">modificados y eliminados</span></p></body></html>", None))
        ___qtablewidgetitem = self.ls_vuelos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Codigo", None));
        ___qtablewidgetitem1 = self.ls_vuelos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Fecha de salida", None));
        ___qtablewidgetitem2 = self.ls_vuelos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Estado", None));
    # retranslateUi

