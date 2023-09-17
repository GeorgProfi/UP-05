import sys
import matplotlib
from PyQt5.QtWidgets import *
from PyQt5 import  QtGui, QtWidgets
import matplotlib.pyplot as plt

import openpyxl
from ui import Ui_mainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi , edgecolor='#36393f')
        self.axes = fig.add_subplot(111)
        fig.patch.set_facecolor('#36393f')
        self.axes.tick_params(axis='x', colors='#36393f')
        self.axes.tick_params(axis='y', colors='#36393f')
        super(MplCanvas, self).__init__(fig)



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_mainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
global canvas

canvas = MplCanvas(width=10, height=10, dpi=100)
graphic = QtWidgets.QVBoxLayout(ui.widget)
graphic.addWidget(canvas)
canvas.draw()

global procentPart, generalPart

#знаения label
ui.Srok.setMaxLength(2)
ui.summa.setText("0")
ui.FirstPay.setText("0")
ui.procentStav.setText("0")
ui.Srok.setText("0")

ui.BT_Export.setVisible(False)
#при выборе Дифференцированого платежа кнопка становится видимой
def VisibleBT ():
    if ui.RB_dif.isChecked() :
        ui.BT_Export.setVisible(True)
    else:
        ui.BT_Export.setVisible(False)

# функция смены Коэфицента, для увеличения диапозона Slider и расчёта
month_OR_year = 12
def mounthORage():
    global month_OR_year
    if  ui.comboBox.currentIndex() == 1:
        month_OR_year = 1
        ui.horizontalSlider_srok.setMaximum(360)
        ui.Srok.setMaxLength(3)
    else:
        month_OR_year = 12
        ui.horizontalSlider_srok.setMaximum(30)
        ui.Srok.setMaxLength(2)
    print(month_OR_year)

def summaslider():
    s = str(ui.horizontalSlider_summa.value() * 100000)
    i = len(s)
    ui.summa.setText(space_in_lineEdit(s,i))

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
    if ui.summa.text() != '' and ui.procentStav.text() != '' and ui.Srok.text() != '' :
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
    print(month_OR_year)
    srok = float(ui.Srok.text()) * month_OR_year
    print(srok)

    if procent<=100 :
        Ostatok = summa - FirstPay
        everyMS = procent / 12 / 100
        generalStav = (1 + everyMS) ** srok
        everyPay = Ostatok * everyMS * generalStav / (generalStav - 1)

        generalPart = summa
        overPay = everyPay * srok - Ostatok
        total = Ostatok + overPay
        procentPart = overPay
        m = 0
        list = [everyPay, overPay, total]
        for m in range(3):
            n = list[m]
            s = str(round(n))
            i = len(s)
            z = space_in_lineEdit(s,i)

            if m == 0:
                ui.EveryPay.setText(z + " Руб.")
            elif m == 1:
                ui.overpay.setText(z + " Руб.")
            elif m == 2:
                ui.allpay.setText(z + " Руб.")
    else:
        QMessageBox.critical(QWidget(), 'Ошибка!', "Процентная ставка больше 30%")

def result_dif ():
    global procentPart, generalPart,srok

    srok = float(ui.Srok.text()) * month_OR_year
    Ostatok = summa - FirstPay
    RavDoli = Ostatok / int(srok)
    OstatokD = Ostatok
    total = 0
    procentPart = 0

    global masI,masPD,masPNO
    masI = []
    masPD = []
    masPNO = []
    for i in range(int(srok)):

        ProcentNaOstatok = OstatokD / 100 * procent / 12
        everyPayDif = RavDoli + ProcentNaOstatok
        OstatokD -= RavDoli

        masI.append(i+1)
        masPD.append(everyPayDif)
        masPNO.append(ProcentNaOstatok)

        if i==0 :
            pay1 = everyPayDif
        elif i== srok-1 :
            pay2 = everyPayDif

        total += everyPayDif
        procentPart += ProcentNaOstatok
    print (pay1,pay2)
    generalPart = summa

    #list = [pay1, pay2, procentPart, total]
    for m in pay1, pay2, procentPart, total:
        #n = list[m]
        s = str(round(m))
        i = len(s)
        z = space_in_lineEdit(s,i)

        if m == pay1:
            pay11 = z
        elif m == pay2:
            ui.EveryPay.setText(pay11 +'...'+ z + " Руб.")
        elif m == procentPart:
            ui.overpay.setText(z + " Руб.")
        elif m == total:
            ui.allpay.setText(z + " Руб.")

# отделение нулей при вводе
def summaLineEdit():
    s = str(ui.summa.text())
    s = s.replace(' ', '')
    i = len(s)
    print(ui.summa.text())
    ui.summa.setText(space_in_lineEdit(s, i))

def Firstpayslider():
    s = str(ui.horizontalSlider_firstpay.value() * 100000)
    i = len(s)
    ui.FirstPay.setText(space_in_lineEdit(s, i))

def FirstPayLineEdit():
    s = str(ui.FirstPay.text())
    s = s.replace(' ', '')
    i = len(s)
    ui.FirstPay.setText(space_in_lineEdit(s,i))

def Export ():
    pressResult()

    window = QFileDialog()
    path = window.getExistingDirectory(window, 'Выберите директорию')
    print(path)
    try:
        if len(str(ui.allpay.text())) != 0 and len(str(ui.EveryPay.text())) != 0 and len(str(ui.overpay.text())) != 0:
            global book
            book1 = openpyxl.Workbook()
            book1.save(path +'/'+'Платёж по месячно.xlsx')
            book1.close()
            book = openpyxl.open(path +'/'+'Платёж по месячно.xlsx')
            sheet = book.active
            # начальные подписи
            sheet['A1'] = 'Месяц'
            sheet['B1'] = 'Ежмесячный платёж'
            sheet['C1'] = 'Доля процентов'
            #записываем данные
            for i in range(int(srok)):
                print(i,'!')
                sheet['A'+ str(i+2)].value = masI[i]
                sheet['B'+ str(i+2)].value = masPD[i]
                sheet['C'+ str(i+2)].value = masPNO[i]
            book.save(path +'/'+'Платёж по месячно.xlsx')

            book.close()
            QMessageBox.information(QWidget(), 'Успех!', ("Ваши расчёты успешно экспортированы в Excel.\n"
                                                         "Путь: " + str(path)))
        else:
            QMessageBox.critical(QWidget(), 'Ошибка!', "Произведите расчёты!")
    except Exception:
       QMessageBox.critical(QWidget(), 'Ошибка!', "Закройте файл перед экспортом")

def diagram():

    if len(str(ui.allpay.text())) != 0 and len(str(ui.EveryPay.text())) != 0 and len(str(ui.overpay.text())) != 0:
        canvas.axes.cla()
        #canvas.vals = [procentPart, generalPart]
        #canvas.labels = ["Проценты", "Основная часть кредита"]
       # fig, ax = plt.subplots()

        #canvas.fig.set_size_inches(100, 100)
        #canvas.ax.pie([procentPart, generalPart], labels=["Проценты", "Основная часть кредита"], autopct='%1.2f%%')
        #canvas.ax.axis("equal")


        _, texts, autotexts = canvas.axes.pie([procentPart, generalPart], labels=["Проценты", "Основная\n часть кредита"], autopct='%1.2f%%')

        for text in texts:
            text.set_color('white')
        canvas.draw()


    else:
        QMessageBox.critical(QWidget(), 'Ошибка!', 'Произведите расчёты!')

def space_in_lineEdit (s,i):
    z = ''
    while i - 3 > 0:
        z = s[i - 3:i] + ' ' + z
        i -= 3
    z = s[0:i] + ' ' + z
    z = z.strip(" ")
    return str(z)

#выбор месяцев или лет
ui.comboBox.currentIndexChanged.connect(mounthORage)
#connect
ui.BT_Export.clicked.connect(Export)
ui.BT_raschet.clicked.connect(pressResult)
ui.BT_raschet.clicked.connect(diagram)
#ui.raschet.clicked.connect(result)
ui.BT_diagram.clicked.connect(diagram)
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
ui.horizontalSlider_stav.valueChanged.connect(lambda: ui.procentStav.setText(str(ui.horizontalSlider_stav.value())))
ui.horizontalSlider_srok.valueChanged.connect(lambda: ui.Srok.setText(str(ui.horizontalSlider_srok.value())))
ui.horizontalSlider_firstpay.valueChanged.connect(lambda: Firstpayslider())
# запрет ввод
ui.DoubleInputValidation = QtGui.QDoubleValidator()
ui.IntInputValidation = QtGui.QIntValidator()

ui.summa.setValidator(ui.IntInputValidation)
ui.procentStav.setValidator(ui.DoubleInputValidation)
ui.Srok.setValidator(ui.IntInputValidation)
ui.FirstPay.setValidator(ui.IntInputValidation)

ui.procentStav.setMaxLength(4)

#выход
sys.exit(app.exec_())