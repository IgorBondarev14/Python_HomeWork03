#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем
#первый и последний элемент, второй и предпоследний и т.д.

N = int(input("Введите размер списка (целое число): "))
while N < 1:
    N = int(input("Введите размер списка (целое число): "))
from random import randint
numbers = []
for i in range(N):
    numbers.append(randint(-N, N))
print(numbers)

composition = []
import math
for i in range(math.ceil(len(numbers) / 2)):
    composition.append(numbers[i] * numbers[N - i - 1])
print(composition)