# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input("Введите размер последовательности: "))
sequence = [None] * (2 * k + 1)
sequence[k] = 0
sequence[k + 1] = sequence[k - 1] =1
for i in range(k + 2, 2 * k + 1):
    sequence[i] = sequence[i - 1] + sequence[i - 2]
for i in range(k - 2, -1, -1):
    sequence[i] = sequence[i + 2] - sequence[i + 1]
print(sequence)
