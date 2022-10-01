# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов 
# списка, стоящих на нечётной позиции.

N = int(input("Введите размер списка (целое число): "))
while N < 1:
    N = int(input("Введите размер списка (целое число): "))
from random import randint, shuffle
numbers = []
for i in range(N):
    numbers.append(randint(-N, N))
print(numbers)
sum = 0
for i in range(1, N):
    if i % 2 != 0:
        sum = sum + numbers[i]
print("Сумма элементов на нечетных позициях равна: " + str(sum))
