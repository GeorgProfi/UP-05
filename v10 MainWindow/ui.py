# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\georg\PycharmProjects\pythonProject\version5\v9MainW\ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1099, 787)
        mainWindow.setStyleSheet("background: #36393f;\n"
"")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 140, 271, 341))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_Summa = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Summa.sizePolicy().hasHeightForWidth())
        self.label_Summa.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.label_Summa.setFont(font)
        self.label_Summa.setStyleSheet("font: 700 13pt \"Nirmala UI\";\n"
"color : #8e9297;")
        self.label_Summa.setObjectName("label_Summa")
        self.verticalLayout_2.addWidget(self.label_Summa)
        self.label_prcent = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_prcent.sizePolicy().hasHeightForWidth())
        self.label_prcent.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.label_prcent.setFont(font)
        self.label_prcent.setStyleSheet("font: 700 13pt \"Nirmala UI\";\n"
"color : #8e9297;")
        self.label_prcent.setObjectName("label_prcent")
        self.verticalLayout_2.addWidget(self.label_prcent)
        self.label_srok = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_srok.sizePolicy().hasHeightForWidth())
        self.label_srok.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.label_srok.setFont(font)
        self.label_srok.setStyleSheet("font: 700 13pt \"Nirmala UI\";\n"
"color : #8e9297;")
        self.label_srok.setObjectName("label_srok")
        self.verticalLayout_2.addWidget(self.label_srok)
        self.label_Firstpay = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Firstpay.sizePolicy().hasHeightForWidth())
        self.label_Firstpay.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.label_Firstpay.setFont(font)
        self.label_Firstpay.setStyleSheet("font: 700 13pt \"Nirmala UI\";\n"
"color : #8e9297;")
        self.label_Firstpay.setObjectName("label_Firstpay")
        self.verticalLayout_2.addWidget(self.label_Firstpay)
        self.RB_Auent = QtWidgets.QRadioButton(self.centralwidget)
        self.RB_Auent.setGeometry(QtCore.QRect(20, 60, 201, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.RB_Auent.setFont(font)
        self.RB_Auent.setStyleSheet("\n"
"QRadioButton{ \n"
"color: red;\n"
"color : #8e9297;\n"
"border-color: #36393f;\n"
"}\n"
"")
        self.RB_Auent.setChecked(True)
        self.RB_Auent.setObjectName("RB_Auent")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(710, 150, 471, 311))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_everyPay = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_everyPay.setStyleSheet("font: 700 13pt \"Nirmala UI\";\n"
"color : #8e9297;")
        self.label_everyPay.setObjectName("label_everyPay")
        self.verticalLayout_3.addWidget(self.label_everyPay)
        self.EveryPay = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EveryPay.sizePolicy().hasHeightForWidth())
        self.EveryPay.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.EveryPay.setFont(font)
        self.EveryPay.setStyleSheet("QLineEdit {\n"
"        border-width: 3px;\n"
"        border-style: solid;\n"
"        border-color: #36393f;\n"
"        color: #fff\n"
"    }\n"
"    QLineEdit:focus {\n"
"        border-color: #36393f;\n"
"    }\n"
"\n"
"")
        self.EveryPay.setText("")
        self.EveryPay.setObjectName("EveryPay")
        self.verticalLayout_3.addWidget(self.EveryPay)
        self.label_overpay = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_overpay.setStyleSheet("font: 700 13pt \"Nirmala UI\";\n"
"color : #8e9297;")
        self.label_overpay.setObjectName("label_overpay")
        self.verticalLayout_3.addWidget(self.label_overpay)
        self.overpay = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.overpay.sizePolicy().hasHeightForWidth())
        self.overpay.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.overpay.setFont(font)
        self.overpay.setStyleSheet("QLineEdit {\n"
"        border-width: 3px;\n"
"        border-style: solid;\n"
"        border-color: #36393f;\n"
"        color: #fff\n"
"    }\n"
"    QLineEdit:focus {\n"
"        border-color: #36393f;\n"
"    }\n"
"\n"
"")
        self.overpay.setObjectName("overpay")
        self.verticalLayout_3.addWidget(self.overpay)
        self.label_AllPay = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.label_AllPay.setFont(font)
        self.label_AllPay.setStyleSheet("font: 700 13pt \"Nirmala UI\";\n"
"color : #8e9297;")
        self.label_AllPay.setObjectName("label_AllPay")
        self.verticalLayout_3.addWidget(self.label_AllPay)
        self.allpay = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.allpay.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allpay.sizePolicy().hasHeightForWidth())
        self.allpay.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.allpay.setFont(font)
        self.allpay.setStyleSheet("QLineEdit {\n"
"        border-width: 3px;\n"
"        border-style: solid;\n"
"        border-color: #36393f;\n"
"        color: #fff\n"
"    }\n"
"    QLineEdit:focus {\n"
"        border-color: #36393f;\n"
"    }\n"
"\n"
"")
        self.allpay.setText("")
        self.allpay.setObjectName("allpay")
        self.verticalLayout_3.addWidget(self.allpay)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(545, 340, 121, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.comboBox.setFont(font)
        self.comboBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.comboBox.setStyleSheet("QComboBox{\n"
"    border-width: 3px;\n"
"    border-style: solid;\n"
"    border-color: #36393f;\n"
"    color : #66676f;\n"
"    }\n"
"\n"
"QComboBox QAbstractItemView {\n"
"  color: rgb(142,146,151);    \n"
"  background-color: #36393f;\n"
"  padding: 10px;\n"
"  selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* только одна линия */\n"
"     border-top-right-radius: 3px; /* тот же радиус закругления что и у QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.BT_Export = QtWidgets.QPushButton(self.centralwidget)
        self.BT_Export.setGeometry(QtCore.QRect(290, 630, 251, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BT_Export.sizePolicy().hasHeightForWidth())
        self.BT_Export.setSizePolicy(sizePolicy)
        self.BT_Export.setStyleSheet("font: 14pt \"Nirmala UI\";\n"
"background: #B0AEB1;\n"
"color: #36393f;\n"
"")
        self.BT_Export.setObjectName("BT_Export")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(290, 150, 251, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.summa = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.summa.sizePolicy().hasHeightForWidth())
        self.summa.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.summa.setFont(font)
        self.summa.setStyleSheet("QLineEdit {\n"
"        border-width: 3px;\n"
"        border-style: solid;\n"
"        border-color: #36393f;\n"
"        color: #fff\n"
"    }\n"
"    QLineEdit:focus {\n"
"        border-color: #36393f;\n"
"    }\n"
"\n"
"")
        self.summa.setInputMask("")
        self.summa.setMaxLength(11)
        self.summa.setObjectName("summa")
        self.verticalLayout.addWidget(self.summa)
        self.horizontalSlider_summa = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider_summa.setStyleSheet("QSlider{\n"
"                background: #36393f;\n"
"            }\n"
"            QSlider::groove:horizontal {  \n"
"                height: 10px;\n"
"                margin: 0px;\n"
"                border-radius: 5px;\n"
"                background: #a5a6a5;\n"
"            }\n"
"            QSlider::handle:horizontal {\n"
"                background: #fff;\n"
"                border: 1px solid #E3DEE2;\n"
"                width: 17px;\n"
"                margin: -5px 0; \n"
"                border-radius: 8px;\n"
"            }\n"
"            QSlider::sub-page:qlineargradient {\n"
"                background: #fff;\n"
"                border-radius: 5px;\n"
"            }\n"
"\n"
"\n"
"")
        self.horizontalSlider_summa.setMaximum(200)
        self.horizontalSlider_summa.setSingleStep(1)
        self.horizontalSlider_summa.setPageStep(1)
        self.horizontalSlider_summa.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_summa.setObjectName("horizontalSlider_summa")
        self.verticalLayout.addWidget(self.horizontalSlider_summa)
        self.procentStav = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.procentStav.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.procentStav.sizePolicy().hasHeightForWidth())
        self.procentStav.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.procentStav.setFont(font)
        self.procentStav.setStyleSheet("QLineEdit {\n"
"        border-width: 3px;\n"
"        border-style: solid;\n"
"        border-color: #36393f;\n"
"        color: #fff\n"
"    }\n"
"    QLineEdit:focus {\n"
"        border-color: #36393f;\n"
"    }\n"
"\n"
"")
        self.procentStav.setInputMask("")
        self.procentStav.setText("")
        self.procentStav.setMaxLength(4)
        self.procentStav.setFrame(False)
        self.procentStav.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.procentStav.setObjectName("procentStav")
        self.verticalLayout.addWidget(self.procentStav)
        self.horizontalSlider_stav = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider_stav.setStyleSheet("QSlider{\n"
"                background: #36393f;\n"
"            }\n"
"            QSlider::groove:horizontal {  \n"
"                height: 10px;\n"
"                margin: 0px;\n"
"                border-radius: 5px;\n"
"                background: #B0AEB1;\n"
"            }\n"
"            QSlider::handle:horizontal {\n"
"                background: #fff;\n"
"                border: 1px solid #E3DEE2;\n"
"                width: 17px;\n"
"                margin: -5px 0; \n"
"                border-radius: 8px;\n"
"            }\n"
"            QSlider::sub-page:qlineargradient {\n"
"                background: #fff;\n"
"                border-radius: 5px;\n"
"            }")
        self.horizontalSlider_stav.setMaximum(30)
        self.horizontalSlider_stav.setSingleStep(1)
        self.horizontalSlider_stav.setPageStep(1)
        self.horizontalSlider_stav.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_stav.setObjectName("horizontalSlider_stav")
        self.verticalLayout.addWidget(self.horizontalSlider_stav)
        self.Srok = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Srok.sizePolicy().hasHeightForWidth())
        self.Srok.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Srok.setFont(font)
        self.Srok.setStyleSheet("QLineEdit {\n"
"        border-width: 3px;\n"
"        border-style: solid;\n"
"        border-color: #36393f;\n"
"        color: #fff\n"
"    }\n"
"    QLineEdit:focus {\n"
"        border-color: #36393f;\n"
"    }\n"
"\n"
"")
        self.Srok.setMaxLength(11)
        self.Srok.setObjectName("Srok")
        self.verticalLayout.addWidget(self.Srok)
        self.horizontalSlider_srok = QtWidgets.QSlider(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_srok.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_srok.setSizePolicy(sizePolicy)
        self.horizontalSlider_srok.setStyleSheet("QSlider{\n"
"                background: #36393f;\n"
"            }\n"
"            QSlider::groove:horizontal {  \n"
"                height: 10px;\n"
"                margin: 0px;\n"
"                border-radius: 5px;\n"
"                background: #B0AEB1;\n"
"            }\n"
"            QSlider::handle:horizontal {\n"
"                background: #fff;\n"
"                border: 1px solid #E3DEE2;\n"
"                width: 17px;\n"
"                margin: -5px 0; \n"
"                border-radius: 8px;\n"
"            }\n"
"            QSlider::sub-page:qlineargradient {\n"
"                background: #fff;\n"
"                border-radius: 5px;\n"
"            }")
        self.horizontalSlider_srok.setMaximum(30)
        self.horizontalSlider_srok.setSingleStep(1)
        self.horizontalSlider_srok.setPageStep(1)
        self.horizontalSlider_srok.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_srok.setObjectName("horizontalSlider_srok")
        self.verticalLayout.addWidget(self.horizontalSlider_srok)
        self.FirstPay = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FirstPay.sizePolicy().hasHeightForWidth())
        self.FirstPay.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.FirstPay.setFont(font)
        self.FirstPay.setStyleSheet("QLineEdit {\n"
"        border-width: 3px;\n"
"        border-style: solid;\n"
"        border-color: #36393f;\n"
"        color: #fff\n"
"    }\n"
"    QLineEdit:focus {\n"
"        border-color: #36393f;\n"
"    }\n"
"\n"
"")
        self.FirstPay.setMaxLength(11)
        self.FirstPay.setObjectName("FirstPay")
        self.verticalLayout.addWidget(self.FirstPay)
        self.horizontalSlider_firstpay = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider_firstpay.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.horizontalSlider_firstpay.setAutoFillBackground(False)
        self.horizontalSlider_firstpay.setStyleSheet("QSlider{\n"
"               background: #36393f;\n"
"            }\n"
"            QSlider::groove:horizontal {  \n"
"                height: 10px;\n"
"                margin: 0px;\n"
"                border-radius: 5px;\n"
"                background: #B0AEB1;\n"
"            }\n"
"            QSlider::handle:horizontal {\n"
"                background: #fff;\n"
"                border: 1px solid #E3DEE2;\n"
"                width: 17px;\n"
"                margin: -5px 0; \n"
"                border-radius: 8px;\n"
"            }\n"
"            QSlider::sub-page:qlineargradient {\n"
"                background: #fff;\n"
"                border-radius: 5px;\n"
"            }")
        self.horizontalSlider_firstpay.setInputMethodHints(QtCore.Qt.ImhNone)
        self.horizontalSlider_firstpay.setMaximum(200)
        self.horizontalSlider_firstpay.setSingleStep(1)
        self.horizontalSlider_firstpay.setPageStep(1)
        self.horizontalSlider_firstpay.setProperty("value", 0)
        self.horizontalSlider_firstpay.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_firstpay.setObjectName("horizontalSlider_firstpay")
        self.verticalLayout.addWidget(self.horizontalSlider_firstpay)
        self.label_Type_Pay = QtWidgets.QLabel(self.centralwidget)
        self.label_Type_Pay.setGeometry(QtCore.QRect(20, 10, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_Type_Pay.setFont(font)
        self.label_Type_Pay.setStyleSheet("color : #8e9297;")
        self.label_Type_Pay.setObjectName("label_Type_Pay")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(290, 550, 251, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.BT_diagram = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BT_diagram.sizePolicy().hasHeightForWidth())
        self.BT_diagram.setSizePolicy(sizePolicy)
        self.BT_diagram.setStyleSheet("font: 14pt \"Nirmala UI\";\n"
"background: #B0AEB1;\n"
"color: #36393f;\n"
"")
        self.BT_diagram.setObjectName("BT_diagram")
        self.gridLayout.addWidget(self.BT_diagram, 1, 1, 1, 1)
        self.BT_raschet = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BT_raschet.sizePolicy().hasHeightForWidth())
        self.BT_raschet.setSizePolicy(sizePolicy)
        self.BT_raschet.setStyleSheet("font: 14pt \"Nirmala UI\";\n"
"background: #B0AEB1;\n"
"color : #36393f")
        self.BT_raschet.setObjectName("BT_raschet")
        self.gridLayout.addWidget(self.BT_raschet, 1, 0, 1, 1)
        self.RB_dif = QtWidgets.QRadioButton(self.centralwidget)
        self.RB_dif.setGeometry(QtCore.QRect(20, 100, 301, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.RB_dif.setFont(font)
        self.RB_dif.setStyleSheet("color : #8e9297;")
        self.RB_dif.setObjectName("RB_dif")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1099, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Ипотечный Калькулятор"))
        self.label_Summa.setText(_translate("mainWindow", "Сумма ипотеки"))
        self.label_prcent.setText(_translate("mainWindow", "Процентую ставку"))
        self.label_srok.setText(_translate("mainWindow", "Срок ипотеки"))
        self.label_Firstpay.setText(_translate("mainWindow", "Первоначальный взнос"))
        self.RB_Auent.setText(_translate("mainWindow", "Аннуитетные"))
        self.label_everyPay.setText(_translate("mainWindow", "Ежемесячный платёж"))
        self.label_overpay.setText(_translate("mainWindow", "Начислено процентов"))
        self.label_AllPay.setText(_translate("mainWindow", "Всего заплачено банку"))
        self.comboBox.setItemText(0, _translate("mainWindow", "Лет"))
        self.comboBox.setItemText(1, _translate("mainWindow", "Месяцев"))
        self.BT_Export.setText(_translate("mainWindow", "Экспорт "))
        self.label_Type_Pay.setText(_translate("mainWindow", "Тип ежемесячных платежей"))
        self.BT_diagram.setText(_translate("mainWindow", "Диаграмма"))
        self.BT_raschet.setText(_translate("mainWindow", "Расчитать "))
        self.RB_dif.setText(_translate("mainWindow", "Дифференцированные"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
