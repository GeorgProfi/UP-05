# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\UP5\ICv10.ui'
#
# Created by: Jora aka Hrisha aka George Profi
#
# WARNING: autor dolboeb


from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(694, 503)
        self.raschet = QtWidgets.QPushButton(Dialog)
        self.raschet.setGeometry(QtCore.QRect(500, 250, 131, 31))
        self.raschet.setStyleSheet("font: 14pt \"Nirmala UI\";\n""")

        self.grafik = QtWidgets.QPushButton(Dialog)
        self.grafik.setGeometry(QtCore.QRect(470, 300, 200, 31))
        self.grafik.setStyleSheet("font: 11pt \"Nirmala UI\";\n""")

        self.difer = QtWidgets.QPushButton(Dialog)
        self.difer.setGeometry(QtCore.QRect(470, 200, 200, 31))
        self.difer.setStyleSheet("font: 11pt \"Nirmala UI\";\n""")

        self.raschet.setObjectName("raschet")
        self.grafik.setObjectName("grafik")
        self.difer.setObjectName("difer")


        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(230, 50, 221, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.summa = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.summa.setObjectName("summa")
        self.verticalLayout.addWidget(self.summa)
        self.procentStav = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.procentStav.setObjectName("procentStav")
        self.verticalLayout.addWidget(self.procentStav)
        self.Srok = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Srok.setObjectName("Srok")
        self.verticalLayout.addWidget(self.Srok)
        self.FirstPay = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.FirstPay.setObjectName("FirstPay")
        self.verticalLayout.addWidget(self.FirstPay)
        self.overpay = QtWidgets.QLineEdit(Dialog)
        self.overpay.setGeometry(QtCore.QRect(230, 327, 221, 22))
        self.overpay.setObjectName("overpay")
        self.label_overpay = QtWidgets.QLabel(Dialog)
        self.label_overpay.setGeometry(QtCore.QRect(20, 327, 181, 20))
        self.label_overpay.setStyleSheet("font: 700 9pt \"Nirmala UI\";")
        self.label_overpay.setObjectName("label_overpay")
        self.allpay = QtWidgets.QLineEdit(Dialog)
        self.allpay.setGeometry(QtCore.QRect(230, 367, 221, 22))
        self.allpay.setText("")
        self.allpay.setObjectName("allpay")
        self.label_AllPay = QtWidgets.QLabel(Dialog)
        self.label_AllPay.setGeometry(QtCore.QRect(20, 367, 181, 20))
        self.label_AllPay.setStyleSheet("font: 700 9pt \"Nirmala UI\";")
        self.label_AllPay.setObjectName("label_AllPay")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 60, 211, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_Summa = QtWidgets.QLabel(self.layoutWidget)
        self.label_Summa.setStyleSheet("font: 700 9pt \"Nirmala UI\";")
        self.label_Summa.setObjectName("label_Summa")
        self.verticalLayout_2.addWidget(self.label_Summa)
        self.label_prcent = QtWidgets.QLabel(self.layoutWidget)
        self.label_prcent.setStyleSheet("font: 700 9pt \"Nirmala UI\";")
        self.label_prcent.setObjectName("label_prcent")
        self.verticalLayout_2.addWidget(self.label_prcent)
        self.label_srok = QtWidgets.QLabel(self.layoutWidget)
        self.label_srok.setStyleSheet("font: 700 9pt \"Nirmala UI\";")
        self.label_srok.setObjectName("label_srok")
        self.verticalLayout_2.addWidget(self.label_srok)
        self.label_Firstpay = QtWidgets.QLabel(self.layoutWidget)
        self.label_Firstpay.setStyleSheet("font: 700 9pt \"Nirmala UI\";")
        self.label_Firstpay.setObjectName("label_Firstpay")
        self.verticalLayout_2.addWidget(self.label_Firstpay)
        self.EveryPay = QtWidgets.QLineEdit(Dialog)
        self.EveryPay.setGeometry(QtCore.QRect(230, 290, 221, 22))
        self.EveryPay.setText("")
        self.EveryPay.setObjectName("EveryPay")
        self.label_everyPay = QtWidgets.QLabel(Dialog)
        self.label_everyPay.setGeometry(QtCore.QRect(20, 290, 181, 20))
        self.label_everyPay.setStyleSheet("font: 700 9pt \"Nirmala UI\";")
        self.label_everyPay.setObjectName("label_everyPay")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ипотечный Калькулятор"))
        self.raschet.setText(_translate("Dialog", "Расчитать "))
        self.grafik.setText(_translate("Dialog", "Отобразить диаграмму "))
        self.label_overpay.setText(_translate("Dialog", "Начислено процентов"))
        self.label_AllPay.setText(_translate("Dialog", "Всего заплачено банку"))
        self.label_Summa.setText(_translate("Dialog", "Сумму ипотеки"))
        self.label_prcent.setText(_translate("Dialog", "Процентую ставку"))
        self.label_srok.setText(_translate("Dialog", "Срок ипотеки"))
        self.label_Firstpay.setText(_translate("Dialog", "Первоначальный взнос"))
        self.label_everyPay.setText(_translate("Dialog", "Ежемесячный платёж"))

        ##############################################
        self.raschet.clicked.connect(self.result)
        self.grafik.clicked.connect(self.diagram)
        self.difer.clicked.connect(self.diferrsch)


    def result (self):
        global procentPart, generalPart

        summa = int(self.summa.text())
        procent = float(self.procentStav.text())
        srok = int(self.Srok.text()) * 12
        FirstPay = int(self.FirstPay.text())
###########
        Ostatok = summa - FirstPay
        everyMS = procent / 12 / 100
        generalStav = (1 + everyMS) ** srok
        everyPay = Ostatok * everyMS * generalStav / (generalStav - 1)

        generalPart = summa
        overPay = everyPay * srok - Ostatok
        total = Ostatok + overPay
        procentPart = overPay

        self.EveryPay.setText(str(round(everyPay))+" Руб.")
        self.overpay.setText(str(round(overPay))+ " Руб.")
        self.allpay.setText(str(round(total))+ " Руб.")

    def diferrsch(self):
################
        global procentPart, generalPart
        summa = int(self.summa.text())
        procent = float(self.procentStav.text())
        srok = int(self.Srok.text()) * 12
        FirstPay = int(self.FirstPay.text())
##################
        Ostatok = summa - FirstPay
        everyMS = procent / 12 / 100
        generalStav = (1 + everyMS) ** srok
        everyPay = Ostatok * everyMS * generalStav / (generalStav - 1)
        Pogdolg = Ostatok / srok
        procentPart = Ostatok * everyMS
        generalPart = everyPay - procentPart
        overPay = everyPay * srok - Ostatok
        total = summa + overPay

##############
        self.EveryPay.setText(str(round(everyPayV1))+" Руб.")
        self.overpay.setText(str(round(overPay))+ " Руб.")
        self.allpay.setText(str(round(total))+ " Руб.")

        #self.diagram()
    def diagram(self):

        vals = [procentPart, generalPart]
        labels = ["Проценты", "Основная часть кредита"]
        fig, ax = plt.subplots()
        fig.set_size_inches(100, 100)
        ax.pie(vals, labels=labels,autopct='%1.2f%%')
        ax.axis("equal")
        plt.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())