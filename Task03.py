# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.

N = int(input("Введите размер списка (целое число): "))
while N < 1:
    N = int(input("Введите размер списка (целое число): "))
import random
numbers = []
for i in range(N):
    numbers.append(round(random.uniform(0, 10), 2))
print("Исходный список - " + str(numbers))

fraction = []
for i in range(N):
    fraction.append(round(numbers[i] % 1, 2))
print("Дробные части - " + str(fraction))
fraction.sort()
print("Упорядоченные дробные части - " + str(fraction))
print("Разница между максимальным и минимальным значением дробной части равна: " \
    + str(fraction[-1] - fraction[0]))