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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(502, 465)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(0, 0, 501, 461))
        self.tabWidget.setMinimumSize(QSize(100, 0))
        self.tabWidget.setMaximumSize(QSize(10000000, 10000000))
        self.tabWidget.setSizeIncrement(QSize(0, 0))
        self.tabWidget.setBaseSize(QSize(0, 0))
        palette = QPalette()
        brush = QBrush(QColor(52, 0, 79, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(232, 228, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(170, 170, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(85, 85, 127, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(113, 113, 170, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush3)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        brush7 = QBrush(QColor(212, 212, 255, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        self.tabWidget.setPalette(palette)
        font = QFont()
        font.setFamily(u"Book Antiqua")
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setStyleSheet(u"background-color: rgb(232, 228, 255);\n"
"border-image: url(:/cct/transparente.png);\n"
"color: rgb(52, 0, 79);")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setIconSize(QSize(80, 16))
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.Piloto = QWidget()
        self.Piloto.setObjectName(u"Piloto")
        self.label = QLabel(self.Piloto)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 20, 131, 131))
        self.label.setPixmap(QPixmap(u":/cct/iconopiloto.jpg"))
        self.formLayoutWidget_11 = QWidget(self.Piloto)
        self.formLayoutWidget_11.setObjectName(u"formLayoutWidget_11")
        self.formLayoutWidget_11.setGeometry(QRect(90, 180, 291, 121))
        self.formLayout_12 = QFormLayout(self.formLayoutWidget_11)
        self.formLayout_12.setObjectName(u"formLayout_12")
        self.formLayout_12.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout_12.setVerticalSpacing(20)
        self.formLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.formLayoutWidget_11)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"background-color: rgb(150, 139, 172);")

        self.formLayout_12.setWidget(0, QFormLayout.LabelRole, self.label_43)

        self.lineEdit_24 = QLineEdit(self.formLayoutWidget_11)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_12.setWidget(0, QFormLayout.FieldRole, self.lineEdit_24)

        self.label_44 = QLabel(self.formLayoutWidget_11)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"background-color: rgb(144, 133, 169);")

        self.formLayout_12.setWidget(1, QFormLayout.LabelRole, self.label_44)

        self.lineEdit_25 = QLineEdit(self.formLayoutWidget_11)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_12.setWidget(1, QFormLayout.FieldRole, self.lineEdit_25)

        self.label_45 = QLabel(self.formLayoutWidget_11)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"background-color: rgb(138, 125, 166);")

        self.formLayout_12.setWidget(2, QFormLayout.LabelRole, self.label_45)

        self.lineEdit_26 = QLineEdit(self.formLayoutWidget_11)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_12.setWidget(2, QFormLayout.FieldRole, self.lineEdit_26)

        self.formLayoutWidget_9 = QWidget(self.Piloto)
        self.formLayoutWidget_9.setObjectName(u"formLayoutWidget_9")
        self.formLayoutWidget_9.setGeometry(QRect(90, 300, 291, 81))
        self.formLayout_13 = QFormLayout(self.formLayoutWidget_9)
        self.formLayout_13.setObjectName(u"formLayout_13")
        self.formLayout_13.setLabelAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.formLayout_13.setVerticalSpacing(20)
        self.formLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.formLayoutWidget_9)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"background-color: rgb(127, 115, 156);")

        self.formLayout_13.setWidget(0, QFormLayout.LabelRole, self.label_46)

        self.label_47 = QLabel(self.formLayoutWidget_9)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"background-color: rgb(123, 115, 149);")

        self.formLayout_13.setWidget(1, QFormLayout.LabelRole, self.label_47)

        self.spinBox_10 = QSpinBox(self.formLayoutWidget_9)
        self.spinBox_10.setObjectName(u"spinBox_10")
        self.spinBox_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_13.setWidget(0, QFormLayout.FieldRole, self.spinBox_10)

        self.dateEdit_9 = QDateEdit(self.formLayoutWidget_9)
        self.dateEdit_9.setObjectName(u"dateEdit_9")
        self.dateEdit_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_13.setWidget(1, QFormLayout.FieldRole, self.dateEdit_9)

        self.bt_registrar_piloto_7 = QPushButton(self.Piloto)
        self.bt_registrar_piloto_7.setObjectName(u"bt_registrar_piloto_7")
        self.bt_registrar_piloto_7.setGeometry(QRect(180, 390, 101, 41))
        self.bt_registrar_piloto_7.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.tabWidget.addTab(self.Piloto, "")
        self.Copiloto = QWidget()
        self.Copiloto.setObjectName(u"Copiloto")
        self.label_2 = QLabel(self.Copiloto)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 20, 131, 131))
        self.label_2.setPixmap(QPixmap(u":/cct/iconopiloto.jpg"))
        self.bt_registrar_piloto_6 = QPushButton(self.Copiloto)
        self.bt_registrar_piloto_6.setObjectName(u"bt_registrar_piloto_6")
        self.bt_registrar_piloto_6.setGeometry(QRect(180, 390, 101, 41))
        self.bt_registrar_piloto_6.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.formLayoutWidget_10 = QWidget(self.Copiloto)
        self.formLayoutWidget_10.setObjectName(u"formLayoutWidget_10")
        self.formLayoutWidget_10.setGeometry(QRect(90, 180, 291, 121))
        self.formLayout_10 = QFormLayout(self.formLayoutWidget_10)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.formLayout_10.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout_10.setVerticalSpacing(20)
        self.formLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.formLayoutWidget_10)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"background-color: rgb(150, 139, 172);")

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.label_35)

        self.lineEdit_21 = QLineEdit(self.formLayoutWidget_10)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_10.setWidget(0, QFormLayout.FieldRole, self.lineEdit_21)

        self.label_36 = QLabel(self.formLayoutWidget_10)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"background-color: rgb(144, 133, 169);")

        self.formLayout_10.setWidget(1, QFormLayout.LabelRole, self.label_36)

        self.lineEdit_22 = QLineEdit(self.formLayoutWidget_10)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_10.setWidget(1, QFormLayout.FieldRole, self.lineEdit_22)

        self.label_39 = QLabel(self.formLayoutWidget_10)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"background-color: rgb(138, 125, 166);")

        self.formLayout_10.setWidget(2, QFormLayout.LabelRole, self.label_39)

        self.lineEdit_23 = QLineEdit(self.formLayoutWidget_10)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_10.setWidget(2, QFormLayout.FieldRole, self.lineEdit_23)

        self.formLayoutWidget_4 = QWidget(self.Copiloto)
        self.formLayoutWidget_4.setObjectName(u"formLayoutWidget_4")
        self.formLayoutWidget_4.setGeometry(QRect(90, 300, 291, 81))
        self.formLayout_9 = QFormLayout(self.formLayoutWidget_4)
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.formLayout_9.setLabelAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.formLayout_9.setVerticalSpacing(20)
        self.formLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.formLayoutWidget_4)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"background-color: rgb(127, 115, 156);")

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.label_34)

        self.label_40 = QLabel(self.formLayoutWidget_4)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"background-color: rgb(123, 115, 149);")

        self.formLayout_9.setWidget(1, QFormLayout.LabelRole, self.label_40)

        self.spinBox_9 = QSpinBox(self.formLayoutWidget_4)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.spinBox_9)

        self.dateEdit_8 = QDateEdit(self.formLayoutWidget_4)
        self.dateEdit_8.setObjectName(u"dateEdit_8")
        self.dateEdit_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_9.setWidget(1, QFormLayout.FieldRole, self.dateEdit_8)

        self.tabWidget.addTab(self.Copiloto, "")
        self.Avion = QWidget()
        self.Avion.setObjectName(u"Avion")
        self.formLayoutWidget_5 = QWidget(self.Avion)
        self.formLayoutWidget_5.setObjectName(u"formLayoutWidget_5")
        self.formLayoutWidget_5.setGeometry(QRect(10, 150, 471, 253))
        self.formLayout_5 = QFormLayout(self.formLayoutWidget_5)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout_5.setVerticalSpacing(20)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.formLayoutWidget_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"background-color: rgb(155, 145, 177);")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.lineEdit = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_14 = QLabel(self.formLayoutWidget_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"background-color: rgb(143, 133, 169);")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.lineEdit_2 = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.lineEdit_10 = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.lineEdit_10)

        self.label_17 = QLabel(self.formLayoutWidget_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"background-color: rgb(124, 115, 152);")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.label_17)

        self.lineEdit_11 = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.lineEdit_11)

        self.label_18 = QLabel(self.formLayoutWidget_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"background-color: rgb(120, 114, 147);")

        self.formLayout_5.setWidget(5, QFormLayout.LabelRole, self.label_18)

        self.lineEdit_12 = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_5.setWidget(5, QFormLayout.FieldRole, self.lineEdit_12)

        self.label_15 = QLabel(self.formLayoutWidget_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"background-color: rgb(139, 128, 168);")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_15)

        self.label_16 = QLabel(self.formLayoutWidget_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"background-color: rgb(131, 119, 161);")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_16)

        self.comboBox_2 = QComboBox(self.formLayoutWidget_5)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.comboBox_2)

        self.bt_registrar_piloto_3 = QPushButton(self.Avion)
        self.bt_registrar_piloto_3.setObjectName(u"bt_registrar_piloto_3")
        self.bt_registrar_piloto_3.setGeometry(QRect(200, 400, 91, 31))
        self.bt_registrar_piloto_3.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.label_3 = QLabel(self.Avion)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 10, 131, 131))
        self.label_3.setPixmap(QPixmap(u":/cct/iconoregistroavion.jpg"))
        self.radioButton = QRadioButton(self.Avion)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(330, 40, 53, 19))
        self.radioButton.setStyleSheet(u"background-color: rgb(224, 184, 210);")
        self.radioButton_2 = QRadioButton(self.Avion)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(330, 70, 71, 20))
        self.radioButton_2.setStyleSheet(u"background-color: rgb(238, 190, 212);")
        self.tabWidget.addTab(self.Avion, "")
        self.Vuelo = QWidget()
        self.Vuelo.setObjectName(u"Vuelo")
        self.crearVuelo = QPushButton(self.Vuelo)
        self.crearVuelo.setObjectName(u"crearVuelo")
        self.crearVuelo.setGeometry(QRect(190, 340, 121, 41))
        self.crearVuelo.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.formLayoutWidget_6 = QWidget(self.Vuelo)
        self.formLayoutWidget_6.setObjectName(u"formLayoutWidget_6")
        self.formLayoutWidget_6.setGeometry(QRect(40, 170, 221, 161))
        self.formLayout_6 = QFormLayout(self.formLayoutWidget_6)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setVerticalSpacing(20)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.formLayoutWidget_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"background-color: rgb(150, 139, 175);")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_19)

        self.dateEdit_3 = QDateEdit(self.formLayoutWidget_6)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.dateEdit_3)

        self.label_21 = QLabel(self.formLayoutWidget_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"background-color: rgb(144, 134, 170);")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_21)

        self.dateEdit_4 = QDateEdit(self.formLayoutWidget_6)
        self.dateEdit_4.setObjectName(u"dateEdit_4")
        self.dateEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.dateEdit_4)

        self.label_23 = QLabel(self.formLayoutWidget_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"background-color: rgb(136, 125, 165);")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.label_23)

        self.lineEdit_13 = QLineEdit(self.formLayoutWidget_6)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.lineEdit_13)

        self.label_24 = QLabel(self.formLayoutWidget_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"background-color: rgb(127, 115, 157);")

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.label_24)

        self.comboBox = QComboBox(self.formLayoutWidget_6)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.comboBox)

        self.formLayoutWidget_7 = QWidget(self.Vuelo)
        self.formLayoutWidget_7.setObjectName(u"formLayoutWidget_7")
        self.formLayoutWidget_7.setGeometry(QRect(60, 40, 181, 71))
        self.formLayout_7 = QFormLayout(self.formLayoutWidget_7)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setVerticalSpacing(20)
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.formLayoutWidget_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"background-color: rgb(229, 182, 207);")

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
        self.label_22.setStyleSheet(u"background-color: rgb(213, 174, 197);")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_22)

        self.timeEdit_2 = QTimeEdit(self.formLayoutWidget_7)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.timeEdit_2)

        self.label_4 = QLabel(self.Vuelo)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(330, 20, 131, 121))
        self.label_4.setPixmap(QPixmap(u":/cct/iconoprogramarvuelo.jpg"))
        self.verticalLayoutWidget = QWidget(self.Vuelo)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(300, 150, 191, 171))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox_3 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.comboBox_3)

        self.comboBox_5 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.comboBox_5)

        self.comboBox_6 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.comboBox_6)

        self.comboBox_4 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.comboBox_4)

        self.tabWidget.addTab(self.Vuelo, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Programar Vuelo", None))
        self.label.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 de licencia", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Horas de Experiencia", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Ultima Revision Medica", None))
        self.bt_registrar_piloto_7.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Piloto), QCoreApplication.translate("MainWindow", u"           Piloto           ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/cct/iconopiloto - copia.jpg\"/></p></body></html>", None))
        self.bt_registrar_piloto_6.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 de licencia", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Horas de Experiencia", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Ultima Revision Medica", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Copiloto), QCoreApplication.translate("MainWindow", u"           Copiloto            ", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ID. Avion", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Modelo", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Peso Nominal", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Capacidad", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Tipo propulsion", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 Motor", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Reacci\u00f3n", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Turbo H\u00e9lice", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"H\u00e9lice", None))

        self.bt_registrar_piloto_3.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_3.setText("")
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Carga", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Pasajeros", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Avion), QCoreApplication.translate("MainWindow", u"           Avion           ", None))
        self.crearVuelo.setText(QCoreApplication.translate("MainWindow", u"Programar Vuelo", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Fecha Salida", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Fecha llegada", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Cod. Vuelo", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Bogot\u00e1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Medell\u00edn", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Hora Salida", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h:mm", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Hora llegada", None))
        self.timeEdit_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h:mm", None))
        self.label_4.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Vuelo), QCoreApplication.translate("MainWindow", u"           Vuelo           ", None))
    # retranslateUi

