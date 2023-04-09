# Вам дан словарь per_cent с распределением процентных ставок по вкладам в различных банках таким образом, что ключ — название банка,
# значение — процент. Напишите программу, в результате которой будет сформирован список deposit значений — накопленные средства
# за год вклада в каждом из банков.
# На вход программы с клавиатуры вводится сумма money, которую человек планирует положить под проценты.

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму, которую планируете положить под проценты: "))

TCB = int((per_cent['ТКБ']) * money*0.01)
SCB = int((per_cent['СКБ']) * money*0.01)
VTB = int((per_cent['ВТБ']) * money*0.01)
SBER = int((per_cent['СБЕР']) * money*0.01)

deposit = [TCB, SCB, VTB, SBER]
print("Накопленные средства за год вклада в каждом из банков: ", deposit)
print("Максимальная сумма, которую вы можете заработать:", max(deposit))