import sys
import matplotlib
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')

from matplotlib.figure import Figure
from ui import Ui_Dialog


app = QtWidgets.QApplication(sys.argv)




Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
global procentPart, generalPart
'''
class Ui_Dialog(object):

    def setupUi(ui, Dialog):

        def __init__(ui):
                # Это здесь нужно для доступа к переменным, методам
                # и т.д. в файле design.py
            super().__init__()
           
'''
ui.grafik_3.setVisible(False)


ui.summa.setText("0")
ui.FirstPay.setText("0")
ui.procentStav.setText("0")
ui.Srok.setText("0")


def VisibleBT ():
    if ui.RB_dif.isChecked() :
        ui.grafik_3.setVisible(True)
    else:
        ui.grafik_3.setVisible(False)





MorA = 12

def mounthORage():
    global MorA
    if  ui.comboBox.currentIndex() == 1:
        MorA = 1
        ui.horizontalSlider_srok.setMaximum(360)
    else:

        MorA = 12
        ui.horizontalSlider_srok.setMaximum(30)

    print(MorA)

def Export ():
    my_file = open("file.txt", "w")


def summaslider():
    s = str(ui.horizontalSlider_summa.value() * 100000)
    i = len(s)
    z = ''
    while i - 3 > 0:
        z = s[i - 3:i] + ' ' + z
        i -= 3
    z = s[0:i] + ' ' + z
    z = z.strip(" ")
    ui.summa.setText(str(z))

def pressResult ():
    try:
        global summa,FirstPay,procent
        summa = (ui.summa.text())
        summa = int(summa.replace(' ', ''))

        FirstPay = (ui.FirstPay.text())
        FirstPay = int(FirstPay.replace(' ', ''))

        procent = ui.procentStav.text()
        procent = float(procent.replace(',', '.'))
    except BaseException :
        pass
    if ui.summa.text() != '' and ui.procentStav.text() != '' and ui.Srok.text() != ' ' :
        if summa != 0 and procent != 0 and float(ui.Srok.text()) != 0:
            if summa > FirstPay:

                if ui.RB_Auent.isChecked() == True:
                    result()
                else:
                    result_dif()

            else:
                QMessageBox.critical(QWidget(), 'Ошибка!', "Первоначальный взнос больше суммы кредита!!!")
        else:
            # уведомление обо ошибке
            QMessageBox.critical(QWidget(), 'Ошибка!', "Значение(я) равно нулю!!!")
    else:
        # уведомление обо ошибке
        QMessageBox.critical(QWidget(), 'Ошибка!', "Значение(я) не введенно !!!")


def result():
    global procentPart, generalPart

                        # ввод данных
    print(MorA)

    srok = float(ui.Srok.text()) * MorA
    print(srok)
                #
    Ostatok = summa - FirstPay
    everyMS = procent / 12 / 100
    generalStav = (1 + everyMS) ** srok
    everyPay = Ostatok * everyMS * generalStav / (generalStav - 1)


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

def result_dif ():
    my_file = open('Дифференцированый платёж помесячно.txt', 'w')
    global procentPart, generalPart
    '''
    summa = (ui.summa.text())
    summa = int(summa.replace(' ', ''))

    FirstPay = (ui.FirstPay.text())
    FirstPay = int(FirstPay.replace(' ', ''))
    print (summa)
    procent = ui.procentStav.text()
    procent = float(procent.replace(',','.'))
    if summa != 0 and procent != 0 and float(ui.Srok.text()) != 0:
        if summa > FirstPay:
                        # ввод данных
'''

    srok = float(ui.Srok.text()) * MorA

                #
    Ostatok = summa - FirstPay
                #
    RavDoli = Ostatok / int(srok)
    OstatokD = Ostatok
    total = 0
    procentPart = 0



    my_file.write("{:<10}".format('месяц'))
    my_file.write("{:<10}".format('ежемесячный платёж   '))
    my_file.write("{:<10}".format('доля процентов'))
    my_file.write('\n')

    for i in range(int(srok)):


        ProcentNaOstatok = OstatokD / 100 * procent / 12
        everyPayDif = RavDoli + ProcentNaOstatok
        OstatokD -= RavDoli

        my_file.write("{:<10}".format(str(i+1)+' '))
        my_file.write("{:<10}".format(str(round(everyPayDif,2))+'               '))
        my_file.write("{:<10}".format(str(round(ProcentNaOstatok,2))+'   '))
        my_file.write('\n')
        '''everyPayDif, ProcentNaOstatok'''
        #print(i ,  everyPayDif, ProcentNaOstatok)
        if i==0 :
            pay1 = everyPayDif
        elif i== srok-1 :
            pay2 = everyPayDif

        total += everyPayDif
        procentPart += ProcentNaOstatok
    my_file.close()
    print (pay1,pay2)

    generalPart = summa


    # добовляем пробелы в вывод, цикл сделан что бы уменьшить код, он проганяет 3
    # значения по 1 алгаритм отделяния строк

    m = 0
    list = [pay1, pay2, procentPart, total]
    for m in range(4):
        n = list[m]
        s = str(round(n))
        i = len(s)
        z = ''
        while i - 3 > 0:
            z = s[i - 3:i] + ' ' + z
            i -= 3
        z = s[0:i] + ' ' + z
        z = z.strip(" ")

                    # вывод данных ()

        if m == 0:
            pay11 = z

        elif m == 1:
            ui.EveryPay.setText(pay11 +'...'+ z + " Руб.")
        elif m == 2:
            ui.overpay.setText(z + " Руб.")
        elif m == 3:
            ui.allpay.setText(z + " Руб.")
            '''                #
        else:

            QMessageBox.critical(QWidget(), 'Ошибка!', "Первоначальный взнос больше суммы кредита!!!")
    else:
                    # уведомление обо ошибке
        QMessageBox.critical(QWidget(), 'Ошибка!', "Значение(я) равно нулю!!!")
'''


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
    if len(str(ui.allpay.text())) != 0 and len(str(ui.EveryPay.text())) != 0 and len(str(ui.overpay.text())) != 0:

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
ui.comboBox.currentIndexChanged.connect(mounthORage)
        #connect
ui.raschet.clicked.connect(pressResult)
#ui.raschet.clicked.connect(result)
ui.grafik.clicked.connect(diagram)
ui.RB_dif.toggled.connect(VisibleBT)
ui.RB_Auent.toggled.connect(VisibleBT)
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

ui.DoubleInputValidation = QtGui.QDoubleValidator()
ui.IntInputValidation = QtGui.QIntValidator()

ui.summa.setValidator(ui.IntInputValidation)
ui.procentStav.setValidator(ui.DoubleInputValidation)
ui.Srok.setValidator(ui.IntInputValidation)
ui.FirstPay.setValidator(ui.IntInputValidation)

ui.procentStav.setMaxLength(4)
ui.Srok.setMaxLength(3)

sys.exit(app.exec_())


