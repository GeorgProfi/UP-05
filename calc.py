
summa = int(input('введите сумму ипотеки '))
procent = float(input('введите процент ипотеки '))
srok = int(input('введите срок ипотеки (в годах) ')) * 12
FirstPay = int(input('Введите первоначальный взнос '))
Ostatok = summa - FirstPay
everyMS = procent / 12 / 100
generalStav = (1+everyMS) ** srok
everyPay = Ostatok * everyMS  * generalStav / (generalStav-1)
procentPart = Ostatok * everyMS
generalPart = everyPay - procentPart
overPay = everyPay  * srok - Ostatok
total = summa + overPay
print ('ежемесячный платёж:',round(everyPay))
print ('Переплата :',round(overPay))
print ('Всего заплачено банку:',round(total))
