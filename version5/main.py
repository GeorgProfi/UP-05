import sys
from ui import *
import ui

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from ui import Ui_Dialog

app = QtWidgets.QApplication(sys.argv)




Dialog = QtWidgets.QDialog()
app.setWindowIcon(QtGui.QIcon("bug.ico"))
Dialog.setWindowIcon(QtGui.QIcon("bug.ico"))
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


'''
class Ui_Dialog(object):

    def setupUi(ui, Dialog):

        def __init__(ui):
                # Это здесь нужно для доступа к переменным, методам
                # и т.д. в файле design.py
            super().__init__()
           
'''



ui.summa.setText("0")
ui.FirstPay.setText("0")
ui.procentStav.setText("0")
ui.Srok.setText("0")

global MorA
MorA = 1

def mounthORage():

    if ui.comboBox.currentIndex() == 0:
        MorA = 1
        ui.horizontalSlider_srok.setMaximum(360)
    else:
        MorA = 12
        ui.horizontalSlider_srok.setMaximum(30)
    print(MorA)


def summaslider():
    s = str(ui.horizontalSlider_summa.value() * 100000)
    i = len(s)
    print(ui.horizontalSlider_summa.value())
    z = ''
    while i - 3 > 0:
        z = s[i - 3:i] + ' ' + z
        i -= 3
    z = s[0:i] + ' ' + z
    z = z.strip(" ")
    ui.summa.setText(str(z))

def result():

    summa = (ui.summa.text())
    summa = int(summa.replace(' ', ''))

    FirstPay = (ui.FirstPay.text())
    FirstPay = int(FirstPay.replace(' ', ''))

    if summa != 0 and float(ui.procentStav.text()) != 0 and float(ui.Srok.text()) != 0:
        if summa > FirstPay:
                        # ввод данных

            procent = float(ui.procentStav.text())
            srok = float(ui.Srok.text()) * MorA

                        #
            Ostatok = summa - FirstPay
            everyMS = procent / 12 / 100
            generalStav = (1 + everyMS) ** srok
            everyPay = Ostatok * everyMS * generalStav / (generalStav - 1)
            global procentPart, generalPart

            generalPart = summa
            overPay = everyPay * srok - Ostatok
            total = Ostatok + overPay
            procentPart = overPay

            # добовляем пробелы в вывод, цикл сделан что бы уменьшить код, он проганяет 3
            # значения по 1 алгаритм отделяния строк

            m = 0
            list = [everyPay, overPay, total]
            for m in range(3):
                n = list[m]
                s = str(round(n))
                i = len(s)
                z = ''
                while i - 3 > 0:
                    z = s[i - 3:i] + ' ' + z
                    i -= 3
                z = s[0:i] + ' ' + z
                z = z.strip(" ")

                            #
                            # вывод данных ()
                if m == 0:
                    ui.EveryPay.setText(z + " Руб.")
                elif m == 1:
                    ui.overpay.setText(z + " Руб.")
                elif m == 2:
                    ui.allpay.setText(z + " Руб.")
                            #
        else:

            QMessageBox.critical(QWidget(), 'Ошибка!', "Первоначальный взнос больше суммы кредита!!!")
    else:
                    # уведомление обо ошибке
        QMessageBox.critical(QWidget(), 'Ошибка!', "Значение(я) равно нулю!!!")

def summaLineEdit():

    s = str(ui.summa.text())
    s = s.replace(' ', '')
    i = len(s)
    print(ui.summa.text())
    z = ''
    while i - 3 > 0:
        z = s[i - 3:i] + ' ' + z
        i -= 3
    z = s[0:i] + ' ' + z
    z = z.strip(" ")
    ui.summa.setText(str(z))

def stavslider():
    ui.procentStav.setText(str(ui.horizontalSlider_stav.value()))

def srokslider():
    ui.Srok.setText(str(ui.horizontalSlider_srok.value()))

def Firstpayslider():
    s = str(ui.horizontalSlider_firstpay.value() * 100000)
    i = len(s)

    z = ''
    while i - 3 > 0:
        z = s[i - 3:i] + ' ' + z
        i -= 3
    z = s[0:i] + ' ' + z
    z = z.strip(" ")
    ui.FirstPay.setText(str(z))
def FirstPayLineEdit():

    s = str(ui.FirstPay.text())
    s = s.replace(' ', '')
    i = len(s)
    z = ''
    while i - 3 > 0:
        z = s[i - 3:i] + ' ' + z
        i -= 3
    z = s[0:i] + ' ' + z
    z = z.strip(" ")
    ui.FirstPay.setText(str(z))

            #

def diagram():
    if len(str(ui.allpay.text())) != 0 and len(str(ui.EveryPay.text())) != 0 and len(
            str(ui.overpay.text())) != 0:

            vals = [procentPart, generalPart]
            labels = ["Проценты", "Основная часть кредита"]
            fig, ax = plt.subplots()
            fig.set_size_inches(100, 100)
            ax.pie(vals, labels=labels, autopct='%1.2f%%')
            ax.axis("equal")
            plt.show()

    else:
        QMessageBox.critical(QWidget(), 'Ошибка!', "Введите данные!!!")

#выбр месяцов или лет
ui.comboBox.currentIndexChanged.connect(mounthORage)
        #connect
ui.raschet.clicked.connect(result)
ui.grafik.clicked.connect(diagram)
            # ui.difer.clicked.connect(self.diferrsch)
ui.summa.textEdited.connect(summaLineEdit)
ui.FirstPay.textEdited.connect(FirstPayLineEdit)

            # ReadOnly для выходных данных
ui.EveryPay.setReadOnly(True)
ui.allpay.setReadOnly(True)
ui.overpay.setReadOnly(True)
            # изменение lineEdit в реальном времени

ui.horizontalSlider_summa.valueChanged.connect(lambda: summaslider())
ui.horizontalSlider_stav.valueChanged.connect(lambda: stavslider())
ui.horizontalSlider_srok.valueChanged.connect(lambda: srokslider())
ui.horizontalSlider_firstpay.valueChanged.connect(lambda: Firstpayslider())

            # запрет ввод

ui.intInputValidation = QtGui.QIntValidator()
ui.summa.setValidator(ui.intInputValidation)
            #
ui.intInputValidation = QtGui.QIntValidator()
ui.procentStav.setValidator(ui.intInputValidation)

ui.procentStav.setMaxLength(3)

sys.exit(app.exec_())


